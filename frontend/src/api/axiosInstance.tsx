import axios, {AxiosResponse, AxiosError, InternalAxiosRequestConfig} from 'axios';

// Types
interface TokenResponse {
    access: string;
    refresh: string;
}

interface QueueItem {
    resolve: (token: string) => void;
    reject: (error: any) => void;
}

interface CustomAxiosRequestConfig extends InternalAxiosRequestConfig {
    _retry?: boolean;
}

// State management
let isRefreshing = false;
let failedQueue: QueueItem[] = [];

const processQueue = (error: any, token: string | null = null): void => {
    failedQueue.forEach(({resolve, reject}) => {
        if (error) {
            reject(error);
        } else if (token) {
            resolve(token);
        }
    });
    failedQueue = [];
};

const refreshToken = async (): Promise<string> => {
    try {
        const refreshTokenValue = localStorage.getItem('refresh_token');

        if (!refreshTokenValue) {
            throw new Error('No refresh token available');
        }

        const response = await axios.post<TokenResponse>(
            `${process.env.REACT_APP_API_URL || "http://localhost:85/"}token/refresh/`,
            {refresh: refreshTokenValue},
            {
                headers: {'Content-Type': 'application/json'},
                withCredentials: true
            }
        );

        const {access, refresh} = response.data;

        // Store new tokens
        localStorage.setItem('access_token', access);
        localStorage.setItem('refresh_token', refresh);

        // Update default authorization header
        axios.defaults.headers.common['Authorization'] = `Bearer ${access}`;

        // Process queued requests
        processQueue(null, access);

        return access;
    } catch (error) {
        // Clear tokens on refresh failure
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        delete axios.defaults.headers.common['Authorization'];

        processQueue(error);
        throw error;
    }
};

// Response interceptor
axios.interceptors.response.use(
    (response: AxiosResponse) => response,
    async (error: AxiosError) => {
        const originalRequest = error.config as CustomAxiosRequestConfig;

        if (!originalRequest) {
            return Promise.reject(error);
        }

        // Check for 401 unauthorized and ensure we haven't already retried
        if (error.response?.status === 401 && !originalRequest._retry) {
            originalRequest._retry = true;

            // If already refreshing, queue this request
            if (isRefreshing) {
                return new Promise<string>((resolve, reject) => {
                    failedQueue.push({resolve, reject});
                })
                    .then((token: string) => {
                        originalRequest.headers = originalRequest.headers || {};
                        originalRequest.headers['Authorization'] = `Bearer ${token}`;
                        return axios(originalRequest);
                    })
                    .catch((err) => Promise.reject(err));
            }

            isRefreshing = true;

            try {
                const newToken = await refreshToken();

                if (process.env.REACT_APP_DEBUG) {
                    console.log("New set of tokens were received by interceptor");
                }

                // Update the original request with new token
                originalRequest.headers = originalRequest.headers || {};
                originalRequest.headers['Authorization'] = `Bearer ${newToken}`;

                return axios(originalRequest);
            } catch (refreshError) {
                // Handle refresh failure (e.g., redirect to login)
                if (process.env.REACT_APP_DEBUG) {
                    console.error("Token refresh failed:", refreshError);
                }

                // You might want to redirect to login page here
                // window.location.href = '/login';

                return Promise.reject(refreshError);
            } finally {
                isRefreshing = false;
            }
        }

        return Promise.reject(error);
    }
);

// Request interceptor to add auth header to requests
axios.interceptors.request.use(
    (config: InternalAxiosRequestConfig) => {
        const token = localStorage.getItem('access_token');
        if (token && !config.headers['Authorization']) {
            config.headers['Authorization'] = `Bearer ${token}`;
        }
        return config;
    },
    (error) => Promise.reject(error)
);

export default axios;

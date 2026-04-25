import axios from "axios";
import React, { createContext, useContext, useState, ReactNode } from "react";
import { urlLogout } from "../urls";
import { urlLogin } from "../urls";

interface LoginDataInterface {
  username: string;
  password: string;
}

interface AuthContextType {
  isAuthenticated: boolean;
  login: (props: LoginDataInterface) => Promise<LoginResponseInterface>;
  logout: () => Promise<void>;
}

interface AuthProviderProps {
  children: ReactNode;
}

type UserLoginResponseType = {
  id: number;
  username: string;
  email: string;
};

export interface LoginResponseInterface {
  detail: string;
  user: UserLoginResponseType;
}

const AuthContext = createContext<AuthContextType | null>(null);

export const AuthProvider = ({ children }: AuthProviderProps) => {
  const [isAuthenticated, setIsAuthenticated] = useState<boolean>(false);

  const login = async (
    props: LoginDataInterface,
  ): Promise<LoginResponseInterface> => {
    const csrfToken: string | undefined = document.cookie
      .split("; ")
      .find((row) => row.startsWith("csrftoken="))
      ?.split("=")[1];

    const { username, password } = props;

    try {
      const response = await axios.post(
        urlLogin,
        { username, password },
        { withCredentials: true, headers: { "X-CSRFToken": csrfToken ?? "" } },
      );
      setIsAuthenticated(true);
      console.log("setIsAuthenticated in AuthContext");
      console.log(isAuthenticated);
      return response.data;
    } catch (err: any) {
      console.log(err);
      setIsAuthenticated(false);
      throw err;
    }
  };

  const logout = async () => {
    try {
      const response = await axios.post(
        urlLogout,
        {},
        {
          withCredentials: true,
        },
      );
      alert(response.data.detail);
    } finally {
      setIsAuthenticated(false);
    }
  };

  return (
    <AuthContext.Provider value={{ isAuthenticated, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error("useAuth must be used inside AuthProvider");
  }
  return context;
};

import React from "react";
import axios from "axios";
import {useState, useEffect} from "react";


export interface UseDataFetchInterface<T> {
    data: T | null,
    loading: boolean,
    error: any | null,
}

export const useFetchData = <T>(url: string): UseDataFetchInterface<T> => {
    const [data, setData] = useState<T | null>(null);
    const [error, setError] = useState<any | null>(null);
    const [loading, setLoading] = useState<boolean>(true);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get<T>(url);
                setData(response.data);
                console.log(response.data);

            } catch (err: any) {
                console.error(`Error fetching data from ${url}`, err)
                setError(err);
            } finally {
                setLoading(false);
            }
        };
        if (url) {
            fetchData();
        }
    }, [url])

    return {data, loading, error};
}

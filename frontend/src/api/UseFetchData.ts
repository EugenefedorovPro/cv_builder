import React from "react";
import axios from "axios";
import {useState, useEffect} from "react";
import {useLang} from "../contexts/LangContext";


export interface UseDataFetchInterface<T> {
    data: T | null,
    loading: boolean,
    error: any | null,
}

export const useFetchData = <T>(url: string): UseDataFetchInterface<T> => {
    const [data, setData] = useState<T | null>(null);
    const [error, setError] = useState<any | null>(null);
    const [loading, setLoading] = useState<boolean>(true);

    const {lang} = useLang();

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get<T>(url,
                    {params: {lang}}
                );
                setData(response.data);

            } catch (err: any) {
                console.error(`Error fetching data from ${url}`, err)
                const message: string = err?.response?.data?.details || err?.message || "unknown error";
                setError(message);
            } finally {
                setLoading(false);
            }
        };
        if (url) {
            fetchData();
        }
    }, [url, lang])

    return {data, loading, error};
}

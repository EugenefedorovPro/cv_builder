import React from "react";
import axios from "axios";
import { useState, useEffect } from "react";
import { useLang } from "../contexts/LangContext";

export interface UsePostDataInterface<TResponse, TPayload> {
  data: TResponse | null;
  loading: boolean;
  error: string | null;
  postData: (payload: TPayload) => Promise<TResponse | null>;
}

export const usePostData = <TResponse, TPayload>(
  url: string,
): UsePostDataInterface<TResponse, TPayload> => {
  const [data, setData] = useState<TResponse | null>(null);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  const { lang } = useLang();

  const postData = async (payload: TPayload): Promise<TResponse | null> => {
    setLoading(true);
    setError(null);

    try {
      const response = await axios.post<TResponse>(url, payload, {
        params: { lang },
      });
      setData(response.data);
      return response.data;
    } catch (err: any) {
      console.error(`Error processing ${url}`, err);
      const message = err?.data?.details || err?.message || "unknown error";
      setError(message);
      return null;
    } finally {
      setLoading(false);
    }
  };

  return {
    data,
    loading,
    error,
    postData,
  };
};

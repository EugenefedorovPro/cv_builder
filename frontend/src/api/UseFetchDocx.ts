import {useEffect, useState} from "react";
import axios from "axios";

interface UseFetchDocxInterface {
    loading: string;
    error: any | null;
    download: () => void;
}

export const UseFetchDocx = (url: string, filename: string): UseFetchDocxInterface => {
    const [loading, setLoading] = useState<string>("idle");
    const [error, setError] = useState<any | null>(null);

    const download = async () => {
        setLoading("loading...");
        setError(null)

        try {
            const response = await axios.get(url,
                {responseType: "blob"},
            );
            const blob = new Blob([response.data], {
                type: "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            });

            const link = document.createElement("a");
            const downloadUrl = window.URL.createObjectURL(blob);

            link.href = downloadUrl;
            link.setAttribute("download", filename);
            document.body.appendChild(link);
            link.click();
            link.remove();
            window.URL.revokeObjectURL(downloadUrl);
            setLoading("success");

        } catch (err: any) {
            console.error(`Error in UseFetchDocs`, err)

        }

    }


    return {loading, error, download};

}

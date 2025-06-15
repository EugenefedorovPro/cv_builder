import React, {createContext, useContext, useState, ReactNode} from "react";

export type LangValues = "1" | "2" | "3"
export type Lang = "eng" | "ukr" | "rus"
export type LangArray = {
    [key in LangValues]: Lang;
}

interface LangContextType {
    lang: string;
    setLang: (lang: Lang) => void;
}

interface LangProviderProps {
    children: ReactNode,
}

const LangContext = createContext<LangContextType | undefined>(undefined);

export const LangProvider = ({children}: LangProviderProps) => {
    const [lang, setLang] = useState<Lang>("eng");

    return (
        <LangContext.Provider value={{lang, setLang}}>
            {children}
        </LangContext.Provider>
    );
}

export function useLang(): LangContextType {
    const context = useContext(LangContext);
    if (!context) {
        throw Error("useLang must be used within langProvider");
    }
    return context;
}
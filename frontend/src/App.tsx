import React from 'react';
import {BrowserRouter, Route, Routes} from "react-router-dom";
import Layout from "./pages/Layout";

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Layout/>}>
                    <Route index/>
                    <Route/>
                </Route>
            </Routes>
        </BrowserRouter>
    );
}

export default App;

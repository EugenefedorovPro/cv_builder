import React from 'react';
import './App.css';
import {BrowserRouter, Route, Routes} from "react-router-dom";
import "./components/interceptions/Axios";

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/">
                    <Route index/>
                    <Route/>
                </Route>
            </Routes>
        </BrowserRouter>
    );
}

export default App;

import "./App.css";
import React, { useState } from "react";
import axios from "axios";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Main from "./views/Main";
import Detail from "./components/Detail";
import Update from "./components/Update";

function App() {
    return (
        <div className="App">
            <BrowserRouter>
                <Routes>
                    <Route path="/home" element={<Main />} default />
                    <Route path="/people/:id" element={<Detail />} />
                    <Route element={<Update />} path="/people/edit/:id" />
                </Routes>
            </BrowserRouter>
        </div>
    );
}

export default App;

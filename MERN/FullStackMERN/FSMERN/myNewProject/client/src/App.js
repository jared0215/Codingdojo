import "./App.css";
import React, { useState } from "react";
import axios from "axios";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Main from "../views/Main";

function App() {
    return (
        <div className="App">
            <BrowserRouter>
                <Routes>
                    <Route path="/home" element={<Main />} default />
                </Routes>
            </BrowserRouter>
        </div>
    );
}

export default App;

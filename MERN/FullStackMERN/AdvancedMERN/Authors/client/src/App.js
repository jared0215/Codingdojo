import "./App.css";
import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Main from "./views/Main";
import Update from "./components/AuthorUpdate";
import AuthorForm from "./components/AuthorForm";

function App() {
    return (
        <div className="App">
            <BrowserRouter>
                <Routes>
                    <Route path="/authors" element={<Main />} />
                    <Route path="/authors/:id/edit" element={<Update />} />
                </Routes>
            </BrowserRouter>
        </div>
    );
}

export default App;

import "./App.css";
import axios from "axios";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import ProductList from "./components/ProductList";
import ProductForm from "./components/ProductForm";
import ProductDetail from "./components/ProductDetail";
import Main from "./views/Main";
import Update from "./components/ProductUpdate";

const App = () => {
    return (
        <div>
            <BrowserRouter>
                <Routes>
                    <Route element={<Main />} path="/home" default />
                    <Route element={<ProductDetail />} path="/product/:id" />
                    <Route element={<Update />} path="/product/edit/:id" />
                </Routes>
            </BrowserRouter>
        </div>
    );
};
export default App;

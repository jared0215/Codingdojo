import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Search from "./components/Search";

function App() {
    return (
        <BrowserRouter>
            <div className="App">
                <Routes>
                    <Route path="/" element={<Search />} />
                    <Route path="/:searchTerm/:id" element={<Search />} />
                </Routes>
            </div>
        </BrowserRouter>
    );
}

export default App;

import "./App.css";
import {
    BrowserRouter,
    Routes,
    Route,
    Link,
    useParams,
} from "react-router-dom";
import Home from "./components/Home";
import Number from "./components/Number";
import Hello from "./components/Hello";

function App() {
    return (
        <BrowserRouter>
            <div className="App">
                <Routes>
                    <Route path="/home" element={<Home />} />
                    <Route path="/:id" element={<Number />} />
                    <Route path="/hello/:word" element={<Hello />} />
                    <Route
                        path="/hello/:word/:backgroundColor"
                        element={<Hello />}
                    />
                </Routes>
            </div>
        </BrowserRouter>
    );
}

export default App;

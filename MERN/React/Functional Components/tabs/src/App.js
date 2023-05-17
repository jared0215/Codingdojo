import "./App.css";
import Tabs from "./components/TabsArray.js";
import OutputBox from "./components/TabsOutput.js";

function App() {
    return (
        <div className="App">
            <Tabs tabs={["Tab 1", "Tab 2", "Tab 3"]} />
        </div>
    );
}

export default App;

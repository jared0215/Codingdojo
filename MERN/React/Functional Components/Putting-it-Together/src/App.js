import "./App.css";
import People from "./components/People";

function App() {
  return (
    <div className="App">
      <People lname={"Doe"} fname={"Jane"} age={25} hair={"Black"} />
      <People lname={"Smith"} fname={"John"} age={32} hair={"Brown"} />
      <People lname={"Fillmore"} fname={"Millard"} age={64} hair={"Blonde"} />
      <People lname={"Smith"} fname={"Maria"} age={22} hair={"Red"} />
    </div>
  );
}

export default App;

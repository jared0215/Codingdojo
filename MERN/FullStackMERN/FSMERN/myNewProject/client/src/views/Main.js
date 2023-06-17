import React, { useState } from "react";
import axios from "axios";
import PersonForm from "../components/PersonForm";
import PersonList from "../components/PersonList";

// Main is a parent component to PersonForm and PersonList
const Main = (props) => {
    // We are going to use useState to store our list of people
    const [people, setPeople] = useState([]);

    return (
        <div>
            {/* /* PersonForm and Person List can both utilize the getter and setter
            established in their parent component: */}
            <PersonForm people={people} setPeople={setPeople} />
            <hr />
            {/* /* All we need to do is pass the people state variable and the
            setPeople function into each component as props */}
            <PersonList people={people} setPeople={setPeople} />
        </div>
    );
};

// We must export the component to use it in other files
export default Main;

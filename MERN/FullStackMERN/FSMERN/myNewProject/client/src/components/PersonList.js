import React, { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";

const PersonList = (props) => {
    /* We deconstruct getter and setter which were passed down 
    via props by the parent component (app.js) to our child 
    component (PersonList.js). Now we can easily use the getter 
    and setter without having to write props.getter or props.setter every time: */
    const { people, setPeople } = props;

    // We are going to use useEffect to make a GET request to the database
    useEffect(() => {
        axios
            // Get all people from the database
            .get("http://localhost:8000/api/people")
            .then((res) => {
                console.log(res.data);
                // Store the retrieved data in state via the setter
                setPeople(res.data);
            })
            .catch((err) => console.log(err));
    }, []);

    return (
        <div>
            {people.map((person, index) => {
                return (
                    <div key={index}>
                        {" "}
                        {/* /* Like our JSX return, map requires ONE parent element,
                        so let's refactor. */}
                        <p>{person.lastName}</p>
                        <p>{person.firstName}</p>
                        {/* /* Look to Code Block 3. That :id gets its value right
                        here. */
                        /* Clicking this element will assign the "id"
                        param the value of this document's _id field */
                        /* This
                        will take us to a path similar to
                        "localhost:3000/people/627837837af9898989c9848" */}
                        <Link to={`/people/${person._id}`}>
                            {" "}
                            {person.firstName}'s Page!{" "}
                        </Link>
                    </div>
                );
            })}
        </div>
    );
};

export default PersonList;

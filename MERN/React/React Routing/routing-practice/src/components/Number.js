import React from "react";
import { useParams } from "react-router-dom";

const Number = (props) => {
    const { id } = useParams();
    return (
        <div>
            <h1>The number is: {id}</h1>
        </div>
    );
};

export default Number;

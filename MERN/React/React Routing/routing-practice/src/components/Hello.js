import React from "react";
import { useParams } from "react-router-dom";

const Hello = (props) => {
    const { word, backgroundColor } = useParams();

    return (
        <div>
            <h1
                style={{
                    backgroundColor: backgroundColor,
                    color: "blue",
                    border: "2px solid black",
                }}
            >
                The word is: {word}
            </h1>
        </div>
    );
};

export default Hello;

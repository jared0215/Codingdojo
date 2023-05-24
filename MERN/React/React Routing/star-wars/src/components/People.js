import React from "react";
import { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";

const People = ({ responseData }) => {
    const [homeworldName, setHomeworldName] = useState("");
    const [homeworldId, setHomeworldId] = useState("");

    useEffect(() => {
        axios
            .get(responseData.homeworld)
            .then((response) => {
                setHomeworldName(response.data.name);
                const urlParts = response.data.url.split("/");
                const id = urlParts[urlParts.length - 2];
                setHomeworldId(id);
            })
            .catch((error) => console.log(error));
    }, [responseData.homeworld]);

    return (
        <div>
            <h1>{responseData.name}</h1>
            <p>
                <span style={{ fontWeight: "bold" }}>Height:</span>{" "}
                {responseData.height} cm
            </p>
            <p>
                <span style={{ fontWeight: "bold" }}>Hair Color:</span>{" "}
                {responseData.hair_color}
            </p>
            <p>
                <span style={{ fontWeight: "bold" }}>Eye Color:</span>{" "}
                {responseData.eye_color}
            </p>
            <p>
                <span style={{ fontWeight: "bold" }}>Skin Color:</span>{" "}
                {responseData.skin_color}
            </p>
            {homeworldName && (
                <p>
                    <span style={{ fontWeight: "bold" }}>Homeworld:</span>{" "}
                    <Link to={`/planets/${homeworldId}`}>{homeworldName}</Link>
                </p>
            )}
        </div>
    );
};

export default People;

import React from "react";

const formatCredits = (credits) => {
    return credits
        ? credits.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")
        : "unknown";
};

const Starships = ({ responseData }) => {
    return (
        <div>
            <h1>{responseData.name}</h1>
            <p>
                <span style={{ fontWeight: "bold" }}>Cost in Credits:</span>{" "}
                {formatCredits(responseData.cost_in_credits)}
            </p>
            <p>
                <span style={{ fontWeight: "bold" }}>Manufacturer:</span>{" "}
                {responseData.manufacturer}
            </p>
            <p>
                <span style={{ fontWeight: "bold" }}>Length:</span>{" "}
                {responseData.length}m
            </p>
            <p>
                <span style={{ fontWeight: "bold" }}>Passengers:</span>{" "}
                {responseData.passengers}
            </p>
        </div>
    );
};

export default Starships;

import React from "react";

const formatPopulation = (population) => {
    return population
        ? population.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")
        : "unknown";
};

const Planets = ({ responseData }) => {
    const hasSurfaceWater = responseData.surface_water > 0;

    return (
        <div>
            <h1>{responseData.name}</h1>
            <p>
                <span style={{ fontWeight: "bold" }}>Climate:</span>{" "}
                {responseData.climate}
            </p>
            <p>
                <span style={{ fontWeight: "bold" }}>Terrain:</span>{" "}
                {responseData.terrain}
            </p>
            <p>
                <span style={{ fontWeight: "bold" }}>Surface Water:</span>{" "}
                {hasSurfaceWater ? "True" : "False"}
            </p>
            <p>
                <span style={{ fontWeight: "bold" }}>Population:</span>{" "}
                {formatPopulation(responseData.population)}
            </p>
        </div>
    );
};

export default Planets;

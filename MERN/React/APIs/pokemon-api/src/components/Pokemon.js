import React, { useState, useEffect } from "react";

const Pokemon = () => {
    const [pokemonList, setPokemonList] = useState([]);
    useEffect(() => {
        fetch("https://pokeapi.co/api/v2/pokemon/?limit=1281")
            .then((response) => response.json())
            .then((response) => {
                console.log(response);
                setPokemonList(response.results);
            })
            .catch((err) => console.log(err));
    }, []);
    return (
        <div>
            <h1>Pokemon</h1>
            {pokemonList.length > 0 && (
                <ol>
                    {pokemonList.map((pokemon, index) => {
                        return <li key={index}>{pokemon.name}</li>;
                    })}
                </ol>
            )}
        </div>
    );
};

export default Pokemon;

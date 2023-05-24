import React, { useState, useEffect } from "react";
import axios from "axios";

const Pokemon = (props) => {
    const [responseData, setResponseData] = useState({ results: [] });

    useEffect(() => {
        axios
            .get("https://pokeapi.co/api/v2/pokemon/?limit=1281")
            .then((response) => {
                setResponseData(response.data);
            })
            .catch((err) => console.log(err));
    }, []);

    return (
        <div>
            <h1>Pokemon</h1>
            {responseData.results.length > 0 && (
                <ol>
                    {responseData.results.map((pokemon, index) => {
                        return <li key={index}>{pokemon.name}</li>;
                    })}
                </ol>
            )}
        </div>
    );
};
export default Pokemon;

//     const [pokemonList, setPokemonList] = useState([]);
//     useEffect(() => {
//         fetch("https://pokeapi.co/api/v2/pokemon/?limit=1281")
//             .then((response) => response.json())
//             .then((response) => {
//                 console.log(response);
//                 setPokemonList(response.results);
//             })
//             .catch((err) => console.log(err));
//     }, []);
//     return (
//         <div>
//             <h1>Pokemon</h1>
//             {pokemonList.length > 0 && (
//                 <ol>
//                     {pokemonList.map((pokemon, index) => {
//                         return <li key={index}>{pokemon.name}</li>;
//                     })}
//                 </ol>
//             )}
//         </div>
//     );
// };

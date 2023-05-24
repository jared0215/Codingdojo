import React from "react";
import { useState, useEffect } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import Planets from "./Planets";
import People from "./People";
import Starships from "./Starships";

const Search = (props) => {
    const [responseData, setResponseData] = useState({ results: [] });
    const [searchTerm, setSearchTerm] = useState("people");
    const [submittedSearchTerm, setSubmittedSearchTerm] = useState("people");
    const [id, setId] = useState(1);
    const [submittedId, setSubmittedId] = useState(1);
    const navigate = useNavigate();
    const [isSearched, setIsSearched] = useState(false);

    useEffect(() => {
        if (isSearched) {
            axios
                .get(
                    `https://swapi.dev/api/${submittedSearchTerm}/${submittedId}`
                )
                .then((response) => {
                    setResponseData(response.data);
                })
                .catch((err) => console.log(err));
        }
    }, [submittedSearchTerm, submittedId, isSearched]);

    const handleSearch = (e) => {
        setSearchTerm(e.target.value);
    };
    const handleId = (e) => {
        setId(e.target.value);
    };
    const handleSubmit = (e) => {
        e.preventDefault();
        setSubmittedSearchTerm(searchTerm);
        setSubmittedId(id);
        setIsSearched(true);
        navigate(`/${searchTerm}/${id}`);
    };

    return (
        <div style={{ marginTop: "25px" }}>
            <form onSubmit={handleSubmit}>
                <label htmlFor="search">Search for: </label>
                <select id="search" onChange={handleSearch}>
                    <option value="people">People</option>
                    <option value="planets">Planets</option>
                    <option value="starships">Starships</option>
                </select>
                <label htmlFor="id">ID: </label>
                <input type="text" value={id} onChange={handleId} />
                <button type="submit">Search</button>
            </form>
            {isSearched && submittedSearchTerm === "people" && (
                <People responseData={responseData} searchTerm={searchTerm} />
            )}
            {isSearched && submittedSearchTerm === "planets" && (
                <Planets responseData={responseData} searchTerm={searchTerm} />
            )}
            {isSearched && submittedSearchTerm === "starships" && (
                <Starships
                    responseData={responseData}
                    searchTerm={searchTerm}
                />
            )}
        </div>
    );
};

export default Search;

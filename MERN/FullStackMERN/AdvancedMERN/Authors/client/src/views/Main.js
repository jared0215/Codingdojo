import React, { useState, useEffect } from "react";
import axios from "axios";
import AuthorForm from "../components/AuthorForm";
import AuthorList from "../components/AuthorList";
import DeleteButton from "../components/DeleteButton";

const Main = () => {
    const [authorList, setAuthorList] = useState([]);
    const [errors, setErrors] = useState([]);
    useEffect(() => {
        axios
            .get("http://localhost:8000/api/authors")
            .then((res) => {
                setAuthorList(res.data);
            })
            .catch((err) => console.log(err));
    }, []);

    const removeFromDom = (authorId) => {
        axios
            .delete(`http://localhost:8000/api/authors/${authorId}`)
            .then((res) => {
                setAuthorList(
                    authorList.filter((author) => author._id !== authorId)
                );
                console.log(res);
                console.log(authorList);
                console.log(res.data);
            })
            .catch((err) => console.log(err));
    };
    const createAuthor = (authorParam) => {
        axios
            .post("http://localhost:8000/api/authors", authorParam)
            .then((res) => {
                console.log(res);
                console.log(authorList);
                console.log(res.data);
                setAuthorList([...authorList, res.data]);
            })
            .catch((err) => {
                const errorResponse = err.response.data.errors; // Get the errors from err.response.data
                const errorArr = []; // Define a temp error array to push the messages in
                for (const key of Object.keys(errorResponse)) {
                    // Loop through all errors and get the messages
                    errorArr.push(errorResponse[key].message);
                }
                // Set Errors
                setErrors(errorArr);
            });
    };

    return (
        <div>
            <h1>Favorite Authors</h1>
            {errors.length > 0 && (
                <div className="alert alert-danger" role="alert">
                    {errors.join(", ")}
                </div>
            )}
            <AuthorForm onSubmitProp={createAuthor} initialName="" />
            <AuthorList authors={authorList} removeFromDom={removeFromDom} />
        </div>
    );
};

export default Main;

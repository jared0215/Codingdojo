import React, { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import DeleteButton from "./DeleteButton";
import "bootstrap/dist/css/bootstrap.min.css";
import Button from "react-bootstrap/Button";

const AuthorList = (props) => {
    const { authors, removeFromDom } = props;

    // Remove an author from the state

    return (
        <div
            style={{ display: "block", maxWidth: "25%" }}
            className="mx-auto align-center bg-dark p-5 fs-5 text-light rounded d-flex flex-column mt-5"
        >
            <h1>Authors</h1>
            <ul>
                {authors.map((author) => (
                    <p key={author._id}>
                        <Link to={`/authors/${author._id}/edit`}>
                            {author.name}
                        </Link>
                        <DeleteButton
                            authorId={author._id}
                            successCallback={() => removeFromDom(author._id)}
                        />
                    </p>
                ))}
            </ul>
        </div>
    );
};

export default AuthorList;

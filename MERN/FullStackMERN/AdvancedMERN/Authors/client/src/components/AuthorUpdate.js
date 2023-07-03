import React, { useState, useEffect } from "react";
import axios from "axios";
import { useParams, useNavigate } from "react-router-dom";
import AuthorForm from "../components/AuthorForm";

const Update = (props) => {
    const { id } = useParams();
    const [author, setAuthor] = useState({});
    const [loaded, setLoaded] = useState(false);
    const navigate = useNavigate();

    useEffect(() => {
        axios
            .get("http://localhost:8000/api/authors/" + id)
            .then((res) => {
                setAuthor(res.data);
                setLoaded(true);
            })
            .catch((err) => {
                console.log(err);
            });
    }, []);

    const updateAuthor = (author) => {
        axios
            .put(`http://localhost:8000/api/authors/${id}/edit`, author)
            .then((res) => {
                setAuthor(res.data);
                navigate("/authors");
            })
            .catch((err) => {
                console.log(err);
            });
    };

    return (
        <div>
            <h1>Update Author</h1>
            {loaded && (
                <>
                    <AuthorForm
                        onSubmitProp={updateAuthor}
                        initialName={author.name}
                    />
                </>
            )}
        </div>
    );
};

export default Update;

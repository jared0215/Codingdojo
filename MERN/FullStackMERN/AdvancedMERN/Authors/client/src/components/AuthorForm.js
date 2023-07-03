import React, { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import "bootstrap/dist/css/bootstrap.min.css";

const AuthorForm = (props) => {
    const { initialName, onSubmitProp } = props;
    const [name, setName] = useState(initialName);
    const [errors, setErrors] = useState([]);

    const onSubmitHandler = (e) => {
        e.preventDefault();
        onSubmitProp({ name });
    };

    return (
        <div>
            <Form onSubmit={onSubmitHandler}>
                <Form.Group className="mb-3" controlId="formBasicName">
                    <Form.Label>Name:</Form.Label>
                    <Form.Control
                        type="text"
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                    />
                    <Form.Text className="text-muted">
                        {errors.map((err, index) => (
                            <p key={index}>{err}</p>
                        ))}
                    </Form.Text>
                </Form.Group>
                {/* cancel button */}
                <Button variant="secondary" type="button">
                    Cancel
                </Button>
                {/* submit button */}
                <Button variant="primary" type="submit">
                    Submit
                </Button>
            </Form>
        </div>
    );
};

export default AuthorForm;

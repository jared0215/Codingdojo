import React, { useState } from "react";
import axios from "axios";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import InputGroup from "react-bootstrap/InputGroup";
import "bootstrap/dist/css/bootstrap.min.css";

// Product Form Component
const ProductForm = (props) => {
    // sets the state for the form inputs
    const [title, setTitle] = useState("");
    const [price, setPrice] = useState("");
    const [description, setDescription] = useState("");

    // handles the submit button
    const handleSubmit = (e) => {
        e.preventDefault();

        axios
            .post("http://localhost:8000/api/products", {
                title,
                price,
                description,
            })
            .then((res) => {
                console.log(res);
                console.log(res.data);
            })
            .catch((err) => {
                console.log(err);
            });
    };
    // returns the form component to be rendered in the page
    return (
        <div>
            {/* Product Form */}
            <Form
                onSubmit={handleSubmit}
                className="mx-auto m-5 w-25 bg-dark p-5 fs-5 text-light rounded d-flex flex-column"
            >
                {/* Form Title */}
                <h1>Add Product</h1>

                {/* Product Title Input */}
                <Form.Group controlId="formBasicTitle" className="mb-4 mt-2">
                    <Form.Label>Product Title</Form.Label>
                    <Form.Control
                        type="text"
                        value={title}
                        onChange={(e) => setTitle(e.target.value)}
                    />
                </Form.Group>

                {/* Product Description Input */}
                <Form.Group controlId="formBasicDescription" className="mb-4">
                    <Form.Label>Product Description</Form.Label>
                    <Form.Control
                        type="text"
                        value={description}
                        onChange={(e) => setDescription(e.target.value)}
                    />
                </Form.Group>

                {/* Product Price Input */}
                <Form.Group controlId="formBasicPrice" className="mb-4">
                    <Form.Label>Product Price</Form.Label>
                    <Form.Control
                        type="number"
                        value={price}
                        onChange={(e) => setPrice(e.target.value)}
                    />
                </Form.Group>

                {/* Submit Product Button */}
                <Button
                    variant="primary"
                    type="submit"
                    className="mt-4 w-50 mx-auto"
                >
                    Submit Product
                </Button>
            </Form>
        </div>
    );
};

export default ProductForm;

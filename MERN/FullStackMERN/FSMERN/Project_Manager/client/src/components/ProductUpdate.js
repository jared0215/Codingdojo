import React, { useState, useEffect } from "react";
import axios from "axios";
import { useParams, useNavigate } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";

const Update = (props) => {
    const { id } = useParams();
    const navigate = useNavigate();
    const [title, setTitle] = useState("");
    const [price, setPrice] = useState("");
    const [description, setDescription] = useState("");

    useEffect(() => {
        axios
            .get(`http://localhost:8000/api/products/${id}`)
            .then((res) => {
                console.log(res.data);
                setTitle(res.data.title);
                setPrice(res.data.price);
                setDescription(res.data.description);
            })
            .catch((err) => {
                console.log(err);
            });
    }, []);

    const updatedProduct = (e) => {
        e.preventDefault();
        axios
            .patch(`http://localhost:8000/api/products/${id}`, {
                title,
                price,
                description,
            })
            .then((res) => {
                console.log(res.data);
                navigate("/home");
            })
            .catch((err) => {
                console.log(err);
            });
    };

    return (
        <div>
            {/* Product Form */}
            <Form
                onSubmit={updatedProduct}
                className="mx-auto m-5 w-25 bg-dark p-5 fs-5 text-light rounded d-flex flex-column"
            >
                {/* Form Title */}
                <h1>Edit Product</h1>

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
                    Update Product
                </Button>
            </Form>
        </div>
    );
};

export default Update;

import React, { useState, useEffect } from "react";
import axios from "axios";
import { useParams } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import Button from "react-bootstrap/Button";

const ProductDetail = (props) => {
    const { id } = useParams();
    const [product, setProduct] = useState({});
    useEffect(() => {
        axios
            .get(`http://localhost:8000/api/products/${id}`)
            .then((res) => {
                console.log(res.data);
                setProduct(res.data);
            })
            .catch((err) => {
                console.log(err);
            });
    }, []);
    return (
        <div
            style={{ display: "block", maxWidth: "25%" }}
            className="mx-auto align-center bg-dark p-5 fs-5 text-light rounded d-flex flex-column mt-5"
        >
            <h1>{product.title}</h1>
            <p>Product Description: {product.description}</p>
            <p>Product Price: {product.price}</p>
            <Button variant="primary" href="/home">
                {" "}
                Back to Products{" "}
            </Button>
        </div>
    );
};

export default ProductDetail;

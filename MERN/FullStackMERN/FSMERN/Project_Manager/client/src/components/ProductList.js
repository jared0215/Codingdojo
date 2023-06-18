import React, { useState, useEffect } from "react";
import axios from "axios";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import InputGroup from "react-bootstrap/InputGroup";
import "bootstrap/dist/css/bootstrap.min.css";
import { Link } from "react-router-dom";

const ProductList = (props) => {
    const { product, setProduct } = props;

    useEffect(() => {
        axios
            .get("http://localhost:8000/api/products")
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
            <h1 className="mx-auto">All Products</h1>
            {product.map((product, index) => {
                return (
                    <div key={index} className="">
                        <hr />
                        <h3 className="mt-2">{product.title}</h3>
                        <p>$ {product.price}</p>
                        <p>{product.description}</p>
                        {/* Link to product detail */}
                        <Link to={`/product/${product._id}`}>View Detail</Link>
                        <span> | </span>
                        <Link to={`/product/edit/${product._id}`}>Edit</Link>
                    </div>
                );
            })}
        </div>
    );
};

export default ProductList;

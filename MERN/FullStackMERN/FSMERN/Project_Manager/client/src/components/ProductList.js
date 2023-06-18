import React, { useState, useEffect } from "react";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";
import { Link } from "react-router-dom";
import Button from "react-bootstrap/Button";

const ProductList = (props) => {
    const { removeFromDom, product, setProduct } = props;
    const deleteProduct = (productId) => {
        axios
            .delete(`http://localhost:8000/api/products/${productId}`)
            .then((res) => {
                console.log(res.data);
                removeFromDom(productId);
            })
            .catch((err) => {
                console.log(err);
            });
    };

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
                        <span> | </span>
                        <Button
                            variant="danger"
                            type="submit"
                            className="ms-1 w-10 mx-auto"
                            onClick={() => deleteProduct(product._id)}
                        >
                            Delete
                        </Button>
                    </div>
                );
            })}
        </div>
    );
};

export default ProductList;

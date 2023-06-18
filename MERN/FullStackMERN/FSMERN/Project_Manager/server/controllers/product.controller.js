const Product = require("../models/product.model");

// FIND ALL PRODUCTS
module.exports.findAllProducts = (req, res) => {
    Product.find()
        .then((products) => {
            res.status(200).json(products);
        })
        .catch((err) => {
            res.status(500).json(err);
        });
};

// FIND ONE PRODUCT BY ID
module.exports.findProductById = (req, res) => {
    Product.findById(req.params.id)
        .then((product) => {
            res.status(200).json(product);
        })
        .catch((err) => {
            res.status(500).json(err);
        });
};

// CREATE ONE PRODUCT BY ID
module.exports.createProduct = (req, res) => {
    Product.create(req.body)
        .then((product) => {
            res.status(201).json(product);
        })
        .catch((err) => {
            res.status(500).json(err);
        });
};

// UPDATE ONE PRODUCT BY ID
module.exports.updateProduct = (req, res) => {
    Product.findOneAndUpdate({ _id: req.params.id }, req.body, {
        new: true,
    })
        .then((updatedProduct) => {
            res.status(200).json(updatedProduct);
        })
        .catch((err) => {
            res.status(500).json(err);
        });
};

// DELETE ONE PRODUCT BY ID

module.exports.deleteProduct = (req, res) => {
    Product.deleteOne({ _id: req.params.id })
        .then((deletedProduct) => {
            res.status(200).json(deletedProduct);
        })
        .catch((err) => {
            res.status(500).json(err);
        });
};

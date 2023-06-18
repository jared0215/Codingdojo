const ProductController = require("../controllers/product.controller");

// Routes for our Product API
module.exports = (app) => {
    app.get("/api/products/:id", ProductController.findProductById);
    app.post("/api/products/", ProductController.createProduct);
    app.get("/api/products/", ProductController.findAllProducts);
    app.put("/api/products/:id", ProductController.updateProduct);
};

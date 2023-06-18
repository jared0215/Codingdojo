const ProductController = require("../controllers/product.controller");

// Routes for our Product API
module.exports = (app) => {
    app.get("/api/products/:id", ProductController.findProductById);
    app.patch("/api/products/:id", ProductController.updateProduct);
    app.delete("/api/products/:id", ProductController.deleteProduct);
    app.post("/api/products/", ProductController.createProduct);
    app.get("/api/products/", ProductController.findAllProducts);
};

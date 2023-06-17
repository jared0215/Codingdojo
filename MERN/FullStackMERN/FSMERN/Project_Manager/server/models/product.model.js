const mongoose = require("mongoose");

// This will create a database named "product" if one doesn't already exist.:
const ProductSchema = new mongoose.Schema(
    {
        title: { type: String, required: true },
        description: { type: String, required: true },
        price: { type: Number, required: true },
    },
    { timestamps: true }
);

// This is the model we are using to create a new collection in our database named "product":
module.exports = mongoose.model("Product", ProductSchema);

// Require Mongoose to create a model from the Schema
const mongoose = require("mongoose");

// Creating a Joke Schema
const JokeSchema = new mongoose.Schema(
    {
        // Setup and Punchline Objects are required and must be at least 10 and 3 characters long
        setup: {
            type: String,
            required: [true, "Setup is required"],
            minlength: [10, "Setup must be at least 10 characters long"],
        },
        punchline: {
            type: String,
            required: [true, "Punchline is required"],
            minlength: [3, "Punchline must be at least 3 characters long"],
        },
    },
    // Timestamps are automatically added to documents
    { timestamps: true }
);

// Creating a Joke Model from the Joke Schema and exporting it
module.exports = mongoose.model("Joke", JokeSchema);

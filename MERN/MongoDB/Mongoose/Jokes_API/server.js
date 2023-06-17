// Require the Express Module
const express = require("express");

// Create an Express App
const app = express();

// Require the Mongoose Config Module
require("./config/mongoose.config.js");

// Require the CORS Module
app.use(express.json(), express.urlencoded({ extended: true }));

// Require the Joke Routes Module and invoke it with the app variable
const AllMyJokeRoutes = require("./routes/joke.routes.js");
AllMyJokeRoutes(app);

// Listen on port 8000 for connections to run the app
app.listen(8000, () => console.log("The server is all fired up on port 8000"));

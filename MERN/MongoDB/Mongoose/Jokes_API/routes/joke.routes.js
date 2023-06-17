// Require the controller
const JokeController = require("../controllers/joke.controller.js");

// ROUTES
module.exports = (app) => {
    // GET ALL JOKES
    app.get("/api/jokes", JokeController.findAllJokes);
    // GET ONE JOKE
    app.get("/api/jokes/:id", JokeController.findOneJoke);
    // PATCH UPDATE ONE JOKE
    app.patch("/api/jokes/:id", JokeController.updateJoke);
    // POST CREATE NEW JOKE
    app.post("/api/jokes", JokeController.createNewJoke);
    // DELETE JOKE
    app.delete("/api/jokes/:id", JokeController.deleteJoke);
};

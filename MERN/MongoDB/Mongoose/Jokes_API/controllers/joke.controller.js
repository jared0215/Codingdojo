// Require the model so we can use it in the functions below
const Joke = require("../models/joke.model.js");

// FIND ALL JOKES
module.exports.findAllJokes = (req, res) => {
    // Finding all the jokes
    Joke.find()
        // Returning all the jokes as json
        .then((allJokes) => res.json({ jokes: allJokes }))
        // Catching and returning the error message if something goes wrong
        .catch((err) =>
            res.json({ message: "Something went wrong (Find All)", error: err })
        );
};

// FIND ONE JOKE BY ID
module.exports.findOneJoke = (req, res) => {
    // Finding a single joke by it's ID
    Joke.findOne({ _id: req.params.id })
        // Returning the joke as json
        .then((joke) => res.json({ joke: joke }))
        // Catching and returning the error message if something goes wrong
        .catch((err) =>
            res.json({ message: "Something went wrong (Find One)", error: err })
        );
};

// CREATE A NEW JOKE
module.exports.createNewJoke = (req, res) => {
    // req.body will contain the form data from Postman or from React
    const { jokeData } = req.body;
    // Use the Mongoose model to create a joke
    Joke.create(jokeData)
        // Returning the json results to the frontend
        .then((newJoke) => res.json({ joke: newJoke }))
        // Catching and returning the error message if something goes wrong
        .catch((err) =>
            res.json({
                message: "Something went wrong (Create Joke)",
                error: err,
            })
        );
};

// UPDATE A JOKE BY ID
module.exports.updateJoke = (req, res) => {
    // req.body will contain the form data from Postman or from React
    Joke.findOneAndUpdate({ _id: req.params.id }, req.body, {
        // Setting the new joke to be the updated joke
        new: true,
        runValidators: true,
    })
        // Returning the json results to the frontend
        .then((updatedJoke) => res.json({ joke: updatedJoke }))
        // Catching and returning the error message if something goes wrong
        .catch((err) =>
            res.json({
                message: "Something went wrong (Update Joke)",
                error: err,
            })
        );
};

// DELETE A JOKE BY ID
module.exports.deleteJoke = (req, res) => {
    // Delete a joke by it's ID
    Joke.deleteOne({ _id: req.params.id })
        // Returning the json results to the frontend
        .then((result) => res.json({ result: result }))
        // Catching and returning the error message if something goes wrong
        .catch((err) =>
            res.json({
                message: "Something went wrong (Delete Joke)",
                error: err,
            })
        );
};

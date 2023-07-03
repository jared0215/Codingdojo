const Author = require("../models/author.model");

// CREATE
module.exports.createAuthor = (req, res) => {
    Author.create(req.body)
        .then((newAuthor) => {
            res.status(200).json(newAuthor);
        })
        .catch((err) => {
            res.status(500).json(err);
        });
};

// READ ALL
module.exports.findAllAuthors = (req, res) => {
    Author.find()
        .then((allAuthors) => {
            res.status(200).json(allAuthors);
        })
        .catch((err) => {
            res.status(500).json(err);
        });
};

// READ ONE
module.exports.findOneAuthor = (req, res) => {
    Author.findOne({ _id: req.params.id })
        .then((oneAuthor) => {
            res.status(200).json(oneAuthor);
        })
        .catch((err) => {
            res.status(500).json(err);
        });
};

// UPDATE
module.exports.updateAuthor = (req, res) => {
    Author.findOneAndUpdate({ _id: req.params.id }, req.body)
        .then((updatedAuthor) => {
            res.status(200).json(updatedAuthor);
        })
        .catch((err) => {
            res.status(500).json(err);
        });
};

// DELETE
module.exports.deleteAuthor = (req, res) => {
    Author.deleteOne({ _id: req.params.id })
        .then((deletedAuthor) => {
            res.status(200).json(deletedAuthor);
        })
        .catch((err) => {
            res.status(500).json(err);
        });
};

const AuthorController = require("../controllers/author.controller");

// Routes for our Author API
module.exports = (app) => {
    app.put("/api/authors/:id/edit", AuthorController.updateAuthor);
    app.get("/api/authors/:id", AuthorController.findOneAuthor);
    app.delete("/api/authors/:id", AuthorController.deleteAuthor);
    app.post("/api/authors/", AuthorController.createAuthor);
    app.get("/api/authors/", AuthorController.findAllAuthors);
};

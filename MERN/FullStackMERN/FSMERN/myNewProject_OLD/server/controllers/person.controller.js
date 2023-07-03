const Person = require("../models/person.model.js");

module.exports.index = (request, response) => {
    response.json({
        message: "Hello World",
    });
};

// CREATE
module.exports.createPerson = (request, response) => {
    const { firstName, lastName } = request.body;
    Person.create({
        firstName,
        lastName,
    })
        .then((person) => response.json(person))
        .catch((err) => response.json(err));
};

// GET ALL
module.exports.getAllPeople = (request, response) => {
    Person.find({})
        .then((persons) => {
            console.log(persons); //console logs are optional, but they are highly recommended for troubleshooting!
            response.json(persons);
        })
        .catch((err) => {
            console.log(err);
            response.json(err);
        });
};

// GET ONE BY ID
module.exports.getPerson = (request, response) => {
    Person.findById(request.params.id)
        .then((person) => response.json(person))
        .catch((err) => response.json(err));
};

// UPDATE
module.exports.updatePerson = (request, response) => {
    Person.findOneAndUpdate({ _id: request.params.id }, request.body, {
        new: true,
    })
        .then((updatedPerson) => response.json(updatedPerson))
        .catch((err) => response.json(err));
};

// DELETE
module.exports.deletePerson = (request, response) => {
    Person.deleteOne({ _id: request.params.id }) //note: "id" here MUST match id in corresponding route
        .then((deleteConfirmation) => response.json(deleteConfirmation))
        .catch((err) => response.json(err));
};

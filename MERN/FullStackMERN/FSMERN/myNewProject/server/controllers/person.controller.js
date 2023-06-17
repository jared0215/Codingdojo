const Person = require("../models/person.model.js");
module.exports.index = (request, response) => {
    response.json({
        message: "Hello World",
    });
};

module.exports.createPerson = (request, response) => {
    const { firstName, lastName } = request.body;
    Person.create({
        firstName,
        lastName,
    })
        .then((person) => response.json(person))
        .catch((err) => response.json(err));
};

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

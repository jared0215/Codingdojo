const express = require("express");
const { faker } = require("@faker-js/faker");

const app = express();
const port = 8000;

const createUser = () => {
    const newUser = {
        password: faker.internet.password(),
        email: faker.internet.email(),
        phoneNumber: faker.phone.number(),
        lastName: faker.person.lastName(),
        firstName: faker.person.firstName(),
        _id: faker.datatype.uuid(),
    };
    return newUser;
};

const createCompany = () => {
    const newCompany = {
        _id: faker.datatype.uuid(),
        name: faker.company.name(),
        address: {
            street: faker.location.streetAddress(),
            city: faker.location.city(),
            state: faker.location.state(),
            zipCode: faker.location.zipCode(),
            country: faker.location.country(),
        },
    };
    return newCompany;
};

const newFakeUser = createUser();
const newFakeCompany = createCompany();
console.log(newFakeUser);
console.log(newFakeCompany);

app.get("/api/users/new", (req, res) => {
    res.json(newFakeUser);
});

app.get("/api/companies/new", (req, res) => {
    res.json(newFakeCompany);
});

app.get("/api/user/company", (req, res) => {
    res.json({ user: newFakeUser, company: newFakeCompany });
});

app.listen(port, () =>
    console.log(`App listening at http://localhost:${port}`)
);

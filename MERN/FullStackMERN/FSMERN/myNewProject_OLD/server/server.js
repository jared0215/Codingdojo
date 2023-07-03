const express = require("express");
const cors = require("cors");
const app = express();

app.use(cors());
app.use(express.json()); // Express.json() is a middleware that parses the incoming request body into a JavaScript object
app.use(express.urlencoded({ extended: true }));
// Above is another middleware that parses incoming request bodies into a JavaScript object.
// This is for when the request body is a URL encoded string (which is what HTML forms use).
// The extended: true option allows for nested objects in the URL encoded data.
// If you don't have any nested objects, you can use extended: false.

require("./config/mongoose.config"); // This is the file that connects to the database
require("./routes/person.routes")(app); // This is the file that contains all of the routes for the app

app.listen(8000, () => {
    // This is the port number that will be used to access the app in the browser: http://localhost:8000
    console.log("Listening at Port 8000");
});

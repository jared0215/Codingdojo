const mongoose = require("mongoose");
const PersonSchema = new mongoose.Schema(
    {
        firstName: {
            type: String,
            minlegth: [2, "First name must be at least 2 characters long"],
            required: [true, "First name is required"],
        },
        lastName: {
            type: String,
            minlegth: [2, "Last name must be at least 2 characters long"],
            required: [true, "Last name is required"],
        },
        email: { type: String, required: [true, "Email is required"] },
        birthday: { type: Date, required: [true, "Birthday is required"] },
        password: {
            type: String,
            required: [true, "Password is required"],
            minlegth: [8, "Password must be at least 8 characters long"],
            maxlength: [12, "Password must be no more than 12 characters long"],
        },
    },
    { timestamps: true }
);
module.exports = mongoose.model("Person", PersonSchema);

import React, { useState } from "react";

const UserForm = (props) => {
    const [fname, setFname] = useState("");
    const [lname, setLname] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");

    // Handling Errors
    const [hasBeenSubmitted, setHasBeenSubmitted] = useState(false);
    const [fnameError, setFnameError] = useState("");
    const [lnameError, setLnameError] = useState("");
    const [emailError, setEmailError] = useState("");
    const [passwordError, setPasswordError] = useState("");
    const [confirmPasswordError, setConfirmPasswordError] = useState("");

    const createUser = (e) => {
        e.preventDefault();

        const newUser = { fname, lname, email, password };
        console.log("Hello", newUser);
        setFname("");
        setLname("");
        setEmail("");
        setPassword("");
        setHasBeenSubmitted(true);
    };

    const handleFname = (e) => {
        setFname(e.target.value);
        if (e.target.value.length > 0 && e.target.value.length < 2) {
            setFnameError("First Name must be at least 2 characters long");
        } else {
            setFnameError("");
        }
    };
    const handleLname = (e) => {
        setLname(e.target.value);
        if (e.target.value.length > 0 && e.target.value.length < 2) {
            setLnameError("Last Name must be at least 2 characters long");
        } else {
            setLnameError("");
        }
    };
    const handleEmail = (e) => {
        setEmail(e.target.value);
        if (e.target.value.length > 0 && e.target.value.length < 2) {
            setEmailError("Email must be at least 2 characters long");
        } else {
            setEmailError("");
        }
    };
    const handlePass = (e) => {
        setPassword(e.target.value);
        if (e.target.value.length > 0 && e.target.value.length < 8) {
            setPasswordError("Password must be at least 8 characters long");
        } else {
            setPasswordError("");
        }
    };
    const handleConfirmPass = (e) => {
        setConfirmPassword(e.target.value);
        if (e.target.value != password) {
            setConfirmPasswordError("Passwords must match");
        } else {
            setConfirmPasswordError("");
        }
    };
    return (
        <div>
            <form onSubmit={createUser}>
                {hasBeenSubmitted ? (
                    <h3>Thank you for submitting the form!</h3>
                ) : (
                    <h3>Welcome, please submit the form.</h3>
                )}
                <div>
                    <label>First Name: </label>
                    <input type="text" onChange={handleFname} />
                    {fnameError ? <p>{fnameError}</p> : ""}
                </div>
                <div>
                    <label>Last Name: </label>
                    <input type="text" onChange={handleLname} />
                    {lnameError ? <p>{lnameError}</p> : ""}
                </div>
                <div>
                    <label>Email Address: </label>
                    <input type="text" onChange={handleEmail} />
                    {emailError ? <p>{emailError}</p> : ""}
                </div>
                <div>
                    <label>Password: </label>
                    <input type="text" onChange={handlePass} />
                    {passwordError ? <p>{passwordError}</p> : ""}
                </div>
                <div>
                    <label>Confirm Password: </label>
                    <input type="text" onChange={handleConfirmPass} />
                    {confirmPasswordError ? <p>{confirmPasswordError}</p> : ""}
                </div>
                <input type="submit" value="Create User" />
            </form>
            <div>
                <h6>Your Form Data</h6>
                <p>First Name: {fname}</p>
                <p>Last Name: {lname}</p>
                <p>Email Address: {email}</p>
                <p>Password: {password}</p>
            </div>
        </div>
    );
};

export default UserForm;

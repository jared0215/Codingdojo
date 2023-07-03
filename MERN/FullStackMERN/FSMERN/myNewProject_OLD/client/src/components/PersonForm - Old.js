// import React, { useState, useEffect } from "react";
// import axios from "axios";

// // creates a personForm component to be used in App.js
// const PersonForm = () => {
//     // creates a message state variable and a setMessage function to update the state variable
//     const [message, setMessage] = useState("Loading...");
//     // useEffect is called when the component is rendered
//     useEffect(() => {
//         // makes a get request to the backend api
//         axios
//             .get("http://localhost:8000/api") // this is the api path we created in person.routes.js
//             .then((res) => setMessage(res.data.message)) // if successful, the response is stored in the message state variable
//             .catch((err) => console.log(err)); // if there is an error, it is logged in the console
//     }, []);

//     // returns the message state variable in an h2 tag
//     return (
//         <div>
//             <h2>Message from the backend: {message}</h2>
//         </div>
//     );
// };
// // exports the personForm component for use in other files
// export default PersonForm;

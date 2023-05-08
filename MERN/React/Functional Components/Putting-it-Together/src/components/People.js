import React, { useState } from "react";

const People = (props) => {
  const [birthday, setBirthday] = useState(props.age);
  return (
    <div>
      <h1>
        {props.lname}, {props.fname}
      </h1>
      <p>Age: {birthday}</p>
      <p>Hair Color: {props.hair}</p>
      <button onClick={(event) => setBirthday(birthday + 1)}>
        Birthday Button for {props.fname} {props.lname}
      </button>
    </div>
  );
};
export default People;

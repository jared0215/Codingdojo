import React, { useState } from "react";

const People = (props) => {
  const [money, setMoney] = useState(props.initialMoney);
  return (
    <div>
      <h1>
        {props.lname}, {props.fname}
      </h1>
      <p>Age: {props.age}</p>
      <p>Hair Color: {props.hair}</p>
      <p>Money: ${money}</p>
      <button onClick={(event) => setMoney(money + 100)}>
        Add Money to {props.fname} {props.lname}(s) Balance
      </button>
    </div>
  );
};
export default People;

import React from "react";

function fiveHeads() {
    return new Promise((resolve, reject) => {
        // your code here!
        let headsCount = 0;
        let attempts = 0;
        while (headsCount < 5) {
            attempts++;
            let result = Math.random();
            if (result < 0.5) {
                headsCount++;
            } else {
                headsCount = 0;
            }
        }
    });
}

fiveHeads()
    .then((res) => console.log(res))
    .catch((err) => console.log(err));
console.log("When does this run now?");

export default Coinflip;

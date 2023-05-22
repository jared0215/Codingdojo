function tossCoin() {
    return Math.random() > 0.5 ? "heads" : "tails";
}

function fiveHeads() {
    return new Promise((resolve, reject) => {
        let headsCount = 0;
        let attempts = 0;
        const intervalId = setInterval(() => {
            let result = tossCoin();
            console.log(`${result} was flipped`);
            if (result === "heads") {
                headsCount++;
                if (headsCount === 5) {
                    clearInterval(intervalId);
                    resolve("Heads Flipped 5 Times");
                }
            } else {
                headsCount = 0;
            }
            attempts++;
            if (attempts > 100) {
                clearInterval(intervalId);
                reject("Attempts exceeded 100 flips");
            }
        }, 100);
    });
}

fiveHeads()
    .then((res) => console.log(res))
    .catch((err) => console.log(err));

console.log("When does this run now?");

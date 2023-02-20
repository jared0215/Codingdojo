console.log("page loaded...");

// Changes Profile Name and Changes it back

function changeName() {
    var element = document.querySelector("#changeme");
    if (element.innerText === "Jane Doe") {
        element.innerText = "John Snow";
    } else if (element.innerText === "John Snow") {
        element.innerText = "Jane Doe";
    } else {
        // do nothing
    }
}

// Removes the User

function removeUser() {
    var element = document.querySelector(".card-list-item");
    element.remove();
}

// Decreases Connection Requests Number

function decrease() {
    var element = document.querySelector(".badge")
    element.innerText--;
}

// Increases Your Connections Number

function increase() {
    var element = document.querySelector("#badge-2")
    element.innerText++;
}
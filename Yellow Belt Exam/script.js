// Removes the Donate Button on Click
function removeDonate() {
    var element = document.querySelector("#removeButton");
    element.remove();
}

// Adds++ Pets to the number of petting(s) on the Profile Cards
function addPets(id) {
    var pets = document.querySelector(`#${id}`);
    pets.innerText++;
}

// Alert user what pet they are looking for
function alertSelection(element) {
    alert("You are looking for a " + element.value);
}
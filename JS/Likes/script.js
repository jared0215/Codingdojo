var countOne = 0;
var countTwo = 0;
var countThree = 0;
var countElementOne = document.querySelector("#more-likes-1");
var countElementTwo = document.querySelector("#more-likes-2");
var countElementThree = document.querySelector("#more-likes-3");


function addLikeOne() {
    countOne++;
    countElementOne.innerText = countOne + " like(s)";
    console.log(countOne);
}
function addLikeTwo() {
    countTwo++;
    countElementTwo.innerText = countTwo + " like(s)";
    console.log(countTwo);
}
function addLikeThree() {
    countThree++;
    countElementThree.innerText = countThree + " like(s)";
    console.log(countThree);
}
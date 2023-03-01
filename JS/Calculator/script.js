
// turning display into a js variable
var displayDiv = document.getElementById("display");
var displayNum = "";
var storeNum = "";
var op = "";





function press(num) {
    // console.log(num);
    displayNum += num;
    displayDiv.innerHTML = displayNum;
}

function clr() {
    displayDiv.innerText = 0;
    displayNum = "";
}

function setOP(operators) {
    op = operators;
    storeNum = displayNum;
    displayNum = "";
    console.log(operators);
}

function calculate() {
    if (op == "+") {
        displayDiv.innerText = parseFloat(storeNum) + parseFloat(displayNum);
    } else if (op == "-") {
        displayDiv.innerText = parseFloat(storeNum) - parseFloat(displayNum);
        displayNum = displayDiv.innerText;
    } else if (op == "*") {
        displayDiv.innerText = parseFloat(storeNum) * parseFloat(displayNum);
        displayNum = displayDiv.innerText;
    } else if (op == "/") {
        displayDiv.innerText = parseFloat(storeNum) / parseFloat(displayNum);
        displayNum = displayDiv.innerText;
    } else {

    }
}
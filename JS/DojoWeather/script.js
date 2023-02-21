// Alerts User when clicking a city
function alertCity(element) {
    alert("You selected " + element.innerText);
}

// Removes the cookie policy message
function removeCookie() {
    var element = document.querySelector(".cookie");
    element.remove();
}


// Converts temperature

var hotElementArr = document.querySelectorAll(".hot");
var coldElementArr = document.querySelectorAll(".cold");
var hotNumberArr = [];
var coldNumberArr = [];

for (var i = 0; i < hotElementArr.length; i++) {
    hotNumberArr.push (
        parseInt (
            hotElementArr[i].innerHTML.substring(0, hotElementArr[i].innerHTML.length - 1)
        )
    )
    // console.log(hotNumberArr)
    coldNumberArr.push (
        parseInt (
            coldElementArr[i].innerHTML.substring(0, coldElementArr[i].innerHTML.length - 1)
        )
    )
}

function convertTemp(selectMenu) {
    var value = selectMenu.value;
    if (value == "F") {
        for (var i = 0; i < hotNumberArr.length; i++) {
            hotNumberArr[i] = Math.round(hotNumberArr[i] * 1.8 + 32);
            coldNumberArr[i] = Math.round(coldNumberArr[i] * 1.8 + 32);
            hotElementArr[i].innerHTML = hotNumberArr[i] + "°";
            coldElementArr[i].innerHTML = coldNumberArr[i] + "°";
        }
    } else {
        for (var i = 0; i < hotNumberArr.length; i++) {
            hotNumberArr[i] = Math.round((hotNumberArr[i] - 32) * .5556);
            coldNumberArr[i] = Math.round((coldNumberArr[i] - 32) * .5556);
            hotElementArr[i].innerHTML = hotNumberArr[i] + "°";
            coldElementArr[i].innerHTML = coldNumberArr[i] + "°";
        }
    }
}


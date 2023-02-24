// Pizza Maker

function pizzaOven(crustType, sauceType, cheeses, toppings) {
    var pizza = {};
    pizza.crustType = crustType;
    pizza.sauceType = sauceType;
    pizza.cheeses = cheeses;
    pizza.toppings = toppings;
    return pizza;
}
var p1 = pizzaOven("deep dish", "traditional", "mozzarella", ["pepperoni", "sausage"]);
console.log(p1);

var p2 = pizzaOven("hand tossed", "marinara", ["mozzarella", "feta"], ["mushrooms", "olives", "onions"]);
console.log(p2);

var p3 = pizzaOven("thin crust", "traditional", "fresh mozzarella", "basil");
console.log(p3);

var p4 = pizzaOven(["New York Style","thin crust"], "marinara", "fresh mozzarella", "pepperoni");
console.log(p4);

// Radnom Pizza Maker Bonus Below

var crustType = ["Thin crust", "Deep dish", "New York Style", "Square", "Sicilian"];
var sauceType = ["Traditional", "Marinara", "White", "Pesto", "No Sauce"];
var cheeses = ["Mozarella", "Fresh Mozzarella", "Feta", "Parmigiano-Reggiano", "Pecorino-Romano", "Gorgonzola"];
var toppings = ["Pepperoni", "Mushrooms", "Onions", "Sausage", "Bacon", "Pineapple", "Green Peppers", "Olives", "Anchovies", "Ham", "Extra Cheese", "Basil", "Chicken"];

function randomPizza(crustType, sauceType, cheeses, toppings) {
    var randomPie = {};
    randomPie.crustType = crustType[Math.floor(Math.random() * crustType.length)];
    randomPie.sauceType = sauceType[Math.floor(Math.random() * sauceType.length)];
    randomPie.cheeses = cheeses[Math.floor(Math.random() * cheeses.length)];
    randomPie.toppings = [];
    for (var i = 0; i < 3; i++) {
        var randomTop = Math.floor(Math.random() * toppings.length);
        randomPie.toppings.push(toppings[randomTop]);
    }
    return randomPie;
}
var ourRandomPizza = randomPizza(crustType, sauceType, cheeses, toppings);
console.log(ourRandomPizza);


// ! BELOW THIS IS CODE THAT RUINED MY BRAIN. IT IS SIMPLY FOR REFLECTION!


// function randomPizza(crustType, sauceType, cheeses, toppings) {
//     var randomPie = {};
//     randomPie.crustType = ["Thin crust", "Deep dish", "New York Style", "Square", "Sicilian"][Math.floor(Math.random() * 5)];
//     randomPie.sauceType = ["Traditional", "Marinara", "White", "Pesto", "No Sauce"][Math.floor(Math.random() * 5)];
//     randomPie.cheeses = ["Mozarella", "Fresh Mozzarella", "Feta", "Parmigiano-Reggiano", "Pecorino-Romano", "Gorgonzola"][Math.floor(Math.random() * 6)];
//     randomPie.toppings = ["Pepperoni", "Mushrooms", "Onions", "Sausage", "Bacon", "Pineapple", "Green Peppers", "Olives", "Anchovies", "Ham", "Extra Cheese", "Basil", "Chicken"][Math.floor(Math.random() * 13) + 13 + 13];
//     return randomPie;
// }

// function pizzaOven(crustType, sauceType, cheeses, toppings) {
//     var pizza = {};
//     pizza.crustType = crustType;
//     pizza.sauceType = sauceType;
//     pizza.cheeses = cheeses;
//     pizza.toppings = toppings;
//     return pizza;
// }
// var youMadeIt = {
//     Crust: ["Thin crust", "Deep dish", "New York Style", "Square", "Sicilian"],
//     "Sauce": ["Traditional", "Marinara", "White", "Pesto", "No Sauce"],
//     "Cheeses": ["Mozarella", "Fresh Mozzarella", "Feta", "Parmigiano-Reggiano", "Pecorino-Romano", "Gorgonzola"],
//     "Toppings": ["Pepperoni", "Mushrooms", "Onions", "Sausage", "Bacon", "Pineapple", "Green Peppers", "Olives", "Anchovies", "Ham", "Extra Cheese", "Basil", "Chicken"],
//     "randomPizzaInfo": function() {
//         console.log(youMadeIt[Math.floor(Math.random() * this.Crust.length)]);
//     }
// }
// youMadeIt.randomPizzaInfo();


// function randomPizza() {
//     var youMadeIt = {
//         "Crust": ["Thin crust", "Deep dish", "New York Style", "Square", "Sicilian"],
//         "Sauce": ["Traditional", "Marinara", "White", "Pesto", "No Sauce"],
//         "Cheeses": ["Mozarella", "Fresh Mozzarella", "Feta", "Parmigiano-Reggiano", "Pecorino-Romano", "Gorgonzola"],
//         "Toppings": ["Pepperoni", "Mushrooms", "Onions", "Sausage", "Bacon", "Pineapple", "Green Peppers", "Olives", "Anchovies", "Ham", "Extra Cheese", "Basil", "Chicken"]
//     };
//     return youMadeIt;
// }
// var ourRandomPizza = randomPizza("Crust" + Math.floor(Math.random("Crust") * 5), "Sauce" + Math.floor(Math.random() * 5), "Cheeses" + Math.floor(Math.random() * 6, "Toppings" + Math.floor(Math.random() * 13 + 13 + 13)));
// console.log(ourRandomPizza);
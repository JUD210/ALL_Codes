// https://www.w3schools.com/js/js_conventions.asp


// Variable and function names written as camelCase
// Global variables written in UPPERCASE (We don't, but it's quite common)
// Constants (like PI) written in UPPERCASE


/* Hyphens in HTML and CSS */

// HTML5: attributes can start with data- (data-quantity, data-price).
// CSS: uses hyphens in property-names (font-size).
// JS: Hyphens are not allowed in JavaScript names because it can be mistaken as subtraction attempts.


/* Underscores: */

// Many programmers prefer to use underscores (date_of_birth), especially in SQL databases.
// Underscores are often used in PHP documentation.


/* PascalCase: */

// PascalCase is often preferred by C programmers.


/* camelCase: */

// camelCase is used by JavaScript itself, by jQuery, and other JavaScript libraries.

// Do not start names with a $ sign. It will put you in conflict with many JavaScript library names.


/* Loading JavaScript in HTML */

// <script src="myscript.js"></script>


/* Accessing HTML Elements */
// If possible, use the same naming convention (as JavaScript) in HTML.

// var obj = getElementById("Demo")
// var obj = getElementById("demo")


// Use Lower Case File Names



// ############################################################

// Variable Names
firstName = "John";
lastName = "Doe";

price = 19.90;
tax = 0.20;

fullPrice = price + (price * tax);


// Spaces Around Operators
var x = y + z;
var values = ["Volvo", "Saab", "Fiat"];


// Code Indentation
// !!! Always use 2 spaces for indentation of code blocks:
function toCelsius(fahrenheit) {
  return (5 / 9) * (fahrenheit - 32);
}


// Statement Rules
var values = ["Volvo", "Saab", "Fiat"];

var person = {
  firstName: "John",
  lastName: "Doe",
  age: 50,
  eyeColor: "blue"
};


// Functions
function toCelsius(fahrenheit) {
  return (5 / 9) * (fahrenheit - 32);
}


// Loops
for (i = 0; i < 5; i++) {
  x += i;
}


// Conditionals
if (time < 20) {
  greeting = "Good day";
} else {
  greeting = "Good evening";
}


// Object
var person = {
  firstName: "John",
  lastName: "Doe",
  age: 50,
  eyeColor: "blue"
};

var person = { firstName: "John", lastName: "Doe", age: 50, eyeColor: "blue" };


// Line Length < 80
// If a JavaScript statement does not fit on one line, the best place to break it is after an operator or a comma.


document.getElementById("demo").innerHTML =
  "Hello Dolly.";

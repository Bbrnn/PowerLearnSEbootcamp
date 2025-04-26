//Variable declaration
let playerName = "Eddy"//Can change
const MAX_LEVEL = 10; //Cannot change
var score = 0; //Avoid using var in modern JS

//String
let greeting = "Hello world";
//Number
let age = 35;
let pi = 3.14;
//Boolean
let isRaining = false;

//Null
let emptyValue= null;
//Undefined
let notAssigned;

//object
let user={name:"Eddy",age:25,role:"Developer"};

//Array
let colors = ["red","blue","green"];


let a = 5;
let b = "5";

// Loose equality
console.log(a == b); // true

// Strict equality
console.log(a === b); // false

// Greater than
console.log(10 > 5); // true




let isAdult = true;
let hasID = false;

// Logical AND
console.log(isAdult && hasID); // false

// Logical OR
console.log(isAdult || hasID); // true

// Logical NOT
console.log(!isAdult); // false

console.log(typeof "Hello"); // string
console.log([] instanceof Array); // true

let x = (2, 3); // x is 3
console.log(x);
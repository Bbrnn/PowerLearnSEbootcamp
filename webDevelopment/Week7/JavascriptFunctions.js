function greet() {
  console.log("Hello, World!");
}
greet(); // Call the function to execute it

//Scope in JS functions
//1. Global Scope: Variables declared outside any function are in the global scope and can be accessed from anywhere in the code.
let globalVar = "I am a global variable "; // Global variable
function showGlobalVar() {
  console.log(globalVar); // Accessing global variable
}
showGlobalVar(); // Call the function to execute it


//2. Local Scope: Variables declared inside a function are in the local scope and can only be accessed within that function.
function showLocalVar() {
  let localVar = "I am a local variable"; // Local variable
  console.log(localVar); // Accessing local variable
}
showLocalVar(); // Call the function to execute it
//console.log(localVar); // This will throw an error because localVar is not defined outside the function

//3. Block Scope: Variables declared with let or const inside a block (e.g., if statement, loop) are in the block scope and can only be accessed within that block.
function showBlockScope() {
  if (true) {
    let blockVar = "I'm a block scoped"
    console.log(blockVar); 
  }// Accessing block scoped variable
 // console.log(blockVar); // This will throw an error because blockVar is not defined outside the block
  }
showBlockScope(); // Call the function to execute it


//Function Parameters
function greet(name) {
  console.log(`Hello, ${name}!`); // Using the parameter in the function
}
greet("Alice")
greet("Bob") // Call the function with different arguments


//Default parameers
function greet(name = "Guest") {
  console.log(`Hello, ${name}!`); // Using the parameter in the function
}
greet();

//Return values from functions
function add(a, b) {
  return a + b; // Returning the sum of a and b
}
let sum = add(5, 3); // Calling the function and storing the return valuec
console.log(sum); // Output: 8

//Returning multiple values from a function
function getCoordinates() {
  return [10, 20]; // Returning an array with multiple values
}
let [x, y] = getCoordinates(); // Destructuring the array to get individual values
console.log(x, y); // Output: 10 20

function getUser() {
  return {
    name: "Alice",
    age: 25,
  }; // Returning an object with multiple values  
}
let user = getUser(); // Storing the returned object
console.log(user.name, user.age); // Output: Alice 25

//Combining scope, parameters, and return values
function calculateArea(length, width) {
  let area = length * width; // Local variable to store the area
  return area; // Returning the area
}
let roomArea = calculateArea(5, 10); // Calling the function and storing the return value
console.log(`Room Area: ${roomArea}`); // Output: Room Area: 50


//Arrow functions
const greet1 = (name) => `Hello, ${name}!`;

console.log(greet1("Alice")); // Output: Hello, Alice!

const square = (num) => num * num;
console.log(square(5)); // Output: 25
 



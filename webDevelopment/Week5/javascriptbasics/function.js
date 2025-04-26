function greet(name) {
  return `Hello, ${name}!`;
}
console.log(greet("Eddy"));

//### **Function Expression**
//A function can be assigned to a variable.
const add = function(a,b) {
  return a + b;
}
console.log(add(3,4));

//Arrow functions
//They provide a concise syntax for writing functions. They are particularly useful for callbacks and one-liners.

//1. Basic arrow function
const multiply = (a,b) => a * b;
console.log(multiply(2,3));
//2.Single parameter
const square = x => x * x
console.log(square(4));

//3. No parameters
const greet1 = () => "Hello, World!"; console.log(greet1()); // Hello, World!

//4.Multiple Statements (use {} and return)
const calculate = (a, b) => {const sum = a + b;  return sum*2;};
console.log(calculate(3,5));

//Parameters ad arguements
function greetUser(firstName, lastName) {
  return`Hello ${firstName} ${lastName}`;

}
console.log(greetUser("Eddy","Lugaye"));

//Scope of variables
let globalVar = "I am global";

function demoScope() {
  let localVar = "I am local";
  console.log(globalVar); // Accessible
  console.log(localVar); // Accessible
}

demoScope();
// console.log(localVar); // Error: localVar is not defined

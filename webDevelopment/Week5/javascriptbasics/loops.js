//for loop
//while loop
//do...while loop
//for...in loop
//for...of loop


for (let i = 1; i <= 5; i++) {
  console.log(`Count: ${i}`); // Output: 1, 2, 3, 4, 5
}

let num = 1;
while (num <= 5) {
  console.log(`Number : ${num}`);
  num++;
}

let count = 6;
do { 
  console.log(`Count: ${count}`);
  count++;
}while (count <= 5);

//The for...in loop is used to iterate over the properties of an object (or indices of an array).
const person = { name: "Eddy", age: 25, role: "Instructor" };
for (let key in person) {
  console.log(`${key}: ${person[key]}`); 
}

//The for...of loop is used to iterate over iterable objects such as arrays, strings, or sets.
const fruits = ["🍎", "🍌", "🍓"];

for (let fruit of fruits) {
  console.log(`I love ${fruit}`);
}

//Break
for (let i = 1; i <= 10; i++) {
  if (i === 5) {
    break; // Stop the loop
  }
  console.log(i);
}

for (let i = 1; i <= 5; i++) {
  if (i === 3) {
    continue; // Skip number 3
  }
  console.log(i);
}

for (let i = 1; i <= 5; i++) {
  for (let j = 1; j <= 5; j++) {
    console.log(`${i} x ${j} = ${i * j}`);
  }
}

//Looping through strings and arrays
const name1 = "Eddy";
for (let char of name1) {
  console.log(char)
}

const numbers = [10,20,30,40];
for (let num of numbers) {
  console.log(num);
}
const button = document.getElementById('myButton');
button.onclick = function() {
    alert('Button was clicked!');
};
const btn = document.getElementById('btn');
btn.addEventListener('click', () =>{
  alert('Button was clicked!');
});
document.addEventListener('click', (e) => {
  console.log(`Mouse clicked at: (${e.clientX}, ${e.clientY})`);

});

const button1 = document.getElementById("colorButton");
button1.onclick = function () {
  document.body.style.backgroundColor = `#${Math.floor(Math.random() * 16777215).toString(16)}`;
};

//onmouseover
const text = document.getElementById("hoverText");
text.onmouseover = function () {
  text.style.color = "red";
  text.style.fontweight = "normal"
};

const input = document.getElementById("nameInput");
const display = document.getElementById("nameDisplay");
input.onchange = function () {
  display.textContent = `Hello, ${input.value}!`;
};

const button2 = document.getElementById("toggleButton");
const text1 = document.getElementById("toggleText");
button2.onclick = function () {
  if (text1.style.display === "none") {
    text1.style.display = "block";
    button2.textContent = "Hide Text";
  } else {
    text1.style.display = "none";
    button2.textContent = "Show Text";
  }
};

//SLider
const slider = document.getElementById("fontSlider");
const text2 = document.getElementById("sliderText");
slider.oninput = function () {
  text2.style.fontSize = `${slider.value}px`;
};

//Modal
const modal = document.getElementById("modal");
const openModal = document.getElementById("openModal");
const closeModal = document.getElementById("closeModal");
openModal.onclick = function () {
  modal.style.display = "block";
};
closeModal.onclick = function () {
  modal.style.display = "none";
};

//form 
const form = document.getElementById("myForm");
const email = document.getElementById("email");
const errorMessage = document.getElementById("errorMessage");
const username = document.getElementById("username");
const validationMessage = document.getElementById('validationMessage');
form.onsubmit = function (event) {
  event.preventDefault(); // Prevent form submission
  //Email validation
  if (!email.value.includes("@")) {
    errorMessage.textContent = "Please enter a valid email address.";
    errorMessage.style.color = "red";
  }
  else {
    errorMessage.textContent = "Email is valid.";
    errorMessage.style.color = "green";
  }
  //Username validation
  if (username.value.length < 5) {
    validationMessage.textContent = "Username must be at least 5 characters long.";
    validationMessage.style.color = "red";
  } else {
    validationMessage.textContent = "Username is valid.";
    validationMessage.style.color = "green";
  }
  //If both emal and username are valid, submit the form
  if (errorMessage.style.color === "green" && validationMessage.style.color === "green") {
    alert("Form submitted successfully!");
    form.reset(); // Reset the form
  }
  //If either email or username is invalid, do not submit the form
  else {
    alert("Please correct the errors before submitting.");
  }

};


username.oninput = function () {
 
};

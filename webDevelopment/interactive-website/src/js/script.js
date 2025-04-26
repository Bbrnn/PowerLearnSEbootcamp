// This file contains JavaScript for handling events and interactivity on the website.

// Function to change button text and color on click
function changeButton() {
    const button = document.getElementById('interactiveButton');
    button.textContent = 'Clicked!';
    button.style.backgroundColor = 'lightblue';
}

// Function to handle hover effects
function handleHover(element) {
    element.style.backgroundColor = 'lightgreen';
}

function handleMouseOut(element) {
    element.style.backgroundColor = '';
}

// Function to detect keypress
function detectKeyPress(event) {
    const output = document.getElementById('keypressOutput');
    output.textContent = `Key pressed: ${event.key}`;
}

// Function for double-click action
function handleDoubleClick() {
    alert('Double-click detected!');
}

// Function for long press action
let pressTimer;
function handleLongPress() {
    pressTimer = setTimeout(() => {
        alert('Long press detected!');
    }, 800);
}

function clearLongPress() {
    clearTimeout(pressTimer);
}

// Form validation functions
function validateForm() {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (!emailPattern.test(email)) {
        alert('Please enter a valid email address.');
        return false;
    }

    if (password.length < 8) {
        alert('Password must be at least 8 characters long.');
        return false;
    }

    alert('Form submitted successfully!');
    return true;
}

// Event listeners
document.getElementById('interactiveButton').addEventListener('click', changeButton);
document.getElementById('hoverElement').addEventListener('mouseover', function() { handleHover(this); });
document.getElementById('hoverElement').addEventListener('mouseout', function() { handleMouseOut(this); });
document.addEventListener('keypress', detectKeyPress);
document.getElementById('interactiveButton').addEventListener('dblclick', handleDoubleClick);
document.getElementById('longPressElement').addEventListener('mousedown', handleLongPress);
document.getElementById('longPressElement').addEventListener('mouseup', clearLongPress);
document.getElementById('form').addEventListener('submit', function(event) {
    event.preventDefault();
    validateForm();
});
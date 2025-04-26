var button = document.querySelector('button');
var box = document.getElementById('changeme');
function changeColor() {
  if (box.style.backgroundColor == "red") { // 
    box.style.backgroundColor = "blue";
  } else {
    box.style.backgroundColor = "red";
  }
};

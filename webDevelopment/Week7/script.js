document.getElementById('animateBtn').addEventListener('click', function() {
  const bx = document.getElementById('box');
  box.classList.toggle('animate');
});

document.getElementById('startAnimation').addEventListener('click', function() {
  const circle = document.getElementById('circle');
  circle.style.animation = "expand 3s ease-in-out forwards";
});

const styleSheet = document.styleSheets[0];
styleSheet.insertRule(`
  @keyframes expand {
  0%{
    transform: scale(1);
  }
    50%{
    transform: scale(1.5);
  }`, styleSheet.cssRules.length);


  const box = document.getElementById("movingBox");
  const pauseButton = document.getElementById("pause");
  const resumeButton = document.getElementById("resume");
  
  pauseButton.addEventListener("click", () => {
    box.style.animationPlayState = "paused";
  });
  
  resumeButton.addEventListener("click", () => {
    box.style.animationPlayState = "running";
  });

  const modal = document.getElementById("modal");
const openModalButton = document.getElementById("openModal");
const closeModalButton = document.getElementById("closeModal");

openModalButton.addEventListener("click", () => {
  modal.classList.add("show");
});

closeModalButton.addEventListener("click", () => {
  modal.classList.remove("show");
});

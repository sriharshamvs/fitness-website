document.addEventListener("DOMContentLoaded", function () {
  var currentUrl = location.pathname.split("/").pop();

  var navLinks = document.querySelectorAll(".nav-link");

  navLinks.forEach(function (navLink) {
    var linkUrl = navLink.getAttribute("href");
    if (linkUrl === currentUrl) {
      navLink.classList.add("active");
    }
  });
});

// Calculate BMI function
function calculateBMI(weight, height, gender, age) {
  const heightInMeters = height / 100;
  const bmi = weight / (heightInMeters * heightInMeters);
  return bmi.toFixed(1);
}

// Event listener for form submission
document.getElementById("bmiForm").addEventListener("submit", function (event) {
  event.preventDefault();

  const weight = parseFloat(document.getElementById("weight").value);
  const height = parseFloat(document.getElementById("height").value);
  const gender = document.getElementById("gender").value;
  const age = parseInt(document.getElementById("age").value);

  const bmi = calculateBMI(weight, height, gender, age);

  document.getElementById(
    "bmiResult"
  ).innerHTML = `<strong>Your BMI is: </strong><span class="highlighted-bmi">${bmi}</span>`;
});

document.addEventListener("DOMContentLoaded", function () {
  const steps = document.querySelectorAll(".step");

  steps.forEach((step) => {
    step.addEventListener("mouseenter", () => {
      step.classList.add("show-description");
    });

    step.addEventListener("mouseleave", () => {
      step.classList.remove("show-description");
    });
  });
});

document.addEventListener("DOMContentLoaded", function () {
  const quoteSlides = document.querySelectorAll(".quote-slide");
  let activeSlideIndex = 0;

  function changeQuote() {
    quoteSlides[activeSlideIndex].classList.remove("active");
    activeSlideIndex = (activeSlideIndex + 1) % quoteSlides.length;
    quoteSlides[activeSlideIndex].classList.add("active");
  }

  setInterval(changeQuote, 5000); // Change quote every 5000 milliseconds (5 seconds)
});

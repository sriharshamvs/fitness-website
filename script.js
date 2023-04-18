// Active navigation pop
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

// Featurettes image animation
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

// Featurettes image animation
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

// Carousel animation
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

// Overall Fitness vs. Obesity Chart
document.addEventListener("DOMContentLoaded", function () {
  const ctx = document.getElementById("fitnessData").getContext("2d");

  const fitnessData = {
    labels: ["Fitness", "Obese"],
    datasets: [
      {
        label: "Population Percentage",
        data: [35, 40],
        backgroundColor: ["rgba(54, 162, 235, 0.2)", "rgba(255, 99, 132, 0.2)"],
        borderColor: ["rgba(54, 162, 235, 1)", "rgba(255, 99, 132, 1)"],
        borderWidth: 1,
      },
    ],
  };

  const chart = new Chart(ctx, {
    type: "bar",
    data: fitnessData,
    options: {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });
});

// Average Exercise Time (Hours/Week) Chart
document.addEventListener("DOMContentLoaded", function () {
  const ctx = document.getElementById("exerciseTimeChart").getContext("2d");

  const exerciseTimeData = {
    labels: ["1990", "2000", "2010", "2020"],
    datasets: [
      {
        label: "Average Time Spent Exercising (hours/week)",
        data: [2.1, 2.6, 3.0, 3.3],
        backgroundColor: "rgba(75, 192, 192, 0.2)",
        borderColor: "rgba(75, 192, 192, 1)",
        borderWidth: 1,
      },
    ],
  };

  const chart = new Chart(ctx, {
    type: "line",
    data: exerciseTimeData,
    options: {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });
});

// Percentage of Physically Active Adults Chart
document.addEventListener("DOMContentLoaded", function () {
  const ctx = document.getElementById("activeAdultsChart").getContext("2d");

  const activeAdultsData = {
    labels: ["1990", "2000", "2010", "2020"],
    datasets: [
      {
        label: "Percentage of Physically Active Adults",
        data: [45, 50, 55, 60],
        backgroundColor: "rgba(255, 206, 86, 0.2)",
        borderColor: "rgba(255, 206, 86, 1)",
        borderWidth: 1,
      },
    ],
  };

  const chart = new Chart(ctx, {
    type: "line",
    data: activeAdultsData,
    options: {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });
});

// Nutrition Chart
document.addEventListener("DOMContentLoaded", function () {
  const ctx = document.getElementById("nutritionChart").getContext("2d");

  const nutritionData = {
    labels: ["Carbohydrates", "Proteins", "Fats"],
    datasets: [
      {
        label: "Percentage of Daily Recommended Intake",
        data: [50, 30, 20],
        backgroundColor: [
          "rgba(255, 99, 132, 0.2)",
          "rgba(54, 162, 235, 0.2)",
          "rgba(255, 206, 86, 0.2)",
        ],
        borderColor: [
          "rgba(255, 99, 132, 1)",
          "rgba(54, 162, 235, 1)",
          "rgba(255, 206, 86, 1)",
        ],
        borderWidth: 1,
      },
    ],
  };

  const chart = new Chart(ctx, {
    type: "pie",
    data: nutritionData,
    options: {
      responsive: true, // Set responsive to true
      maintainAspectRatio: false, // Set maintainAspectRatio to false
    },
  });
});

document.addEventListener("DOMContentLoaded", function () {
  // Get the form element
  const loginForm = document.getElementById("loginForm");

  // Validate form on submit
  loginForm.addEventListener("submit", function (event) {
    event.preventDefault();

    // Get the email and password fields
    const emailInput = document.getElementById("email");
    const passwordInput = document.getElementById("password");

    // Check if email and password are valid
    if (!emailInput.checkValidity() || !passwordInput.checkValidity()) {
      // Show custom error messages if any input is invalid
      if (!emailInput.checkValidity()) {
        emailInput.classList.add("is-invalid");
      } else {
        emailInput.classList.remove("is-invalid");
      }
      if (!passwordInput.checkValidity()) {
        passwordInput.classList.add("is-invalid");
      } else {
        passwordInput.classList.remove("is-invalid");
      }
    } else {
      // If both inputs are valid, submit the form
      loginForm.submit();
    }
  });
});

document.addEventListener("DOMContentLoaded", function () {
  const signupForm = document.getElementById("signupForm");

  if (signupForm) {
    signupForm.addEventListener("submit", function (event) {
      event.preventDefault();

      // Get input elements
      const username = document.getElementById("username");
      const email = document.getElementById("email");
      const password = document.getElementById("password");
      const confirmPassword = document.getElementById("confirm-password");

      // Validate input elements
      let isValid = true;

      if (!username.checkValidity()) {
        username.classList.add("is-invalid");
        isValid = false;
      } else {
        username.classList.remove("is-invalid");
      }

      if (!email.checkValidity()) {
        email.classList.add("is-invalid");
        isValid = false;
      } else {
        email.classList.remove("is-invalid");
      }

      if (!password.checkValidity()) {
        password.classList.add("is-invalid");
        isValid = false;
      } else {
        password.classList.remove("is-invalid");
      }

      if (
        password.value !== confirmPassword.value ||
        !confirmPassword.checkValidity()
      ) {
        confirmPassword.classList.add("is-invalid");
        isValid = false;
      } else {
        confirmPassword.classList.remove("is-invalid");
      }

      // Submit the form if validation passes
      if (isValid) {
        console.log("Form submitted"); // Replace this line with the actual form submission logic
        signupForm.submit();
      }
    });
  }
});

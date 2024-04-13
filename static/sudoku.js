/**
    * Function to display message to the user
    * The function is called to display success or error messages to the user
    * The function takes a message and an optional isError parameter
    * If isError is true, the message is displayed in red, else it is displayed in green
    * The message is displayed in the message area at the top of the page
    * The message is hidden after 5 seconds
**/
function displayMessage(message, isError = true) {
    const messageArea = document.getElementById("message-area");
    messageArea.textContent = message;
    messageArea.style.color = isError ? '#ff4747' : '#4CAF50';  // Red for errors, green for success
    messageArea.style.display = 'block';  // Make the message area visible
    setTimeout(() => {
        messageArea.style.display = 'none';  // Hide after 5 seconds
    }, 5000);
}

/**
    * Function to get hint for the user
    * The function is called when the "Get Hint" button is clicked
    * The function fills in one empty cell in the grid with the correct solution
    * If there are no empty cells left, an alert is displayed
**/
function getHint() {
    var empty_cells = [];
    for (let row = 0; row < 9; row++) {
        for (let col = 0; col < 9; col++) {
            const input = document.querySelector(`input[data-row="${row}"][data-col="${col}"]`);
            if (input.value == '') {
                empty_cells.push([row, col]);
            }
        }
    }
    if (empty_cells.length > 0) {
        const randomCell = empty_cells[Math.floor(Math.random() * empty_cells.length)];
        const row = randomCell[0];
        const col = randomCell[1];
        const input = document.querySelector(`input[data-row="${row}"][data-col="${col}"]`);
        input.value = solution[row][col];
    }
    else {
        displayMessage("No empty cells left to fill.");
    }
}

/**
    * Function to clear the user's input
    * The function is called when the "Clear Board" button is clicked
    * The function clears all the input fields in the grid
**/
function clearBoard() {
    for (let row = 0; row < 9; row++) {
        for (let col = 0; col < 9; col++) {
            const input = document.querySelector(`input[data-row="${row}"][data-col="${col}"]`);
            if (!input.hasAttribute('data-cell') || input.getAttribute('data-cell') === "editable") {
                input.value = '';
            }
        }
    }
}


/**
    * Function to toggle the visibility of the solution grid
    * The solution grid is hidden by default
    * When the "Show Solution" button is clicked, the solution grid is displayed
    * When the "Hide Solution" button is clicked, the solution grid is hidden
**/
function toggleSolution() {
    var solutionGrid = document.getElementById("solutionGrid");
    var toggleBtn = document.getElementById("toggleSolutionBtn");

    // Check if the solution grid is currently displayed
    if (solutionGrid.style.display === "none" || solutionGrid.style.display === "") {
        solutionGrid.style.display = "block"; // Show the solution grid
        toggleBtn.innerText = "Hide Solution"; // Change button text to "Hide Solution"
    } else {
        solutionGrid.style.display = "none"; // Hide the solution grid
        toggleBtn.innerText = "Show Solution"; // Change button text back to "Show Solution"
    }
}

/**
    * Function to validate the user input
    * The function is called when the user enters a value in an input field
    * The function removes any characters that are not digits 1-9
**/
function validateInput(input) {
    // Remove any characters that are not digits 1-9
    input.value = input.value.replace(/[^1-9]/g, '');
}

/**
    * Function to check the user's solution
    * The function is called when the "Check Solution" button is clicked
    * The function checks if the user's solution matches the correct solution
    * If the solution is correct, a congratulatory message is displayed
    * If the solution is incorrect, an alert is displayed
**/
function checkSolution() {
    const userGrid = [];
    for (let row = 0; row < 9; row++) {
        const rowValues = [];
        for (let col = 0; col < 9; col++) {
            const input = document.querySelector(`input[data-row="${row}"][data-col="${col}"]`);
            const value = parseInt(input.value, 10);
            if (!value) {
                displayMessage("The grid is not fully filled.");
                return;
            }
            rowValues.push(value);
        }
        userGrid.push(rowValues);
    }

    for (let row = 0; row < 9; row++) {
        for (let col = 0; col < 9; col++) {
            if (userGrid[row][col] !== solution[row][col]) {
                displayMessage("Your solution is incorrect.");
                return;
            }
        }
    }
    for (let row = 0; row < 9; row++) {
        for (let col = 0; col < 9; col++) {
            const input = document.querySelector(`input[data-row="${row}"][data-col="${col}"]`);
            input.setAttribute('data-cell', 'fixed');
            input.disabled = true;
            input.style.backgroundColor = 'transparent';
        }
    }
    stopTimer();
    const timeSpent = document.getElementById("timer").innerText;
    document.getElementById("congratulationsMessage").innerHTML = `<strong>Congratulations!</strong> Your solution is correct. ${timeSpent}`;
    document.getElementById("congratulationsMessage").style.display = "block";
    var celebrationAudio = document.getElementById("celebrationAudio");
    celebrationAudio.play();
    triggerConfetti();
}

/**
    * Function to trigger the confetti animation
    * The function is called when the user's solution is correct
    * The function uses the confetti-js library to create a confetti animation
**/
function triggerConfetti() {
    confetti({
        particleCount: 150, // Number of particles
        spread: 250, // Spread of particles
        angle: 60, // Angle of spread
        origin: { y: 0.4 }, // Origin point on the Y-axis
        origin: { x: 0.2 },
        colors: ['#bb0000', '#ffffff', '#00bb00'], // Customize colors
    });
    confetti({
        particleCount: 150, // Number of particles
        spread: 250, // Spread of particles
        angle: 60, // Angle of spread
        origin: { y: 0.4 }, // Origin point on the Y-axis
        origin: { x: 0.8 },
        colors: ['#bb0000', '#ffffff', '#00bb00'], // Customize colors
    });
}


// Timer
let startTime;
let timerInterval;
/**
    * Function to update the timer display
    * The function calculates the time elapsed since the timer was started
    * The function updates the timer display every second
**/
function updateTimer() {
    const now = new Date().getTime();
    const distance = now - startTime;
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    document.getElementById("timer").innerText = 'Time: ' +
        (hours < 10 ? "0" : "") + hours + ":" +
        (minutes < 10 ? "0" : "") + minutes + ":" +
        (seconds < 10 ? "0" : "") + seconds;
}

// Function to start the timer
function startTimer() {
    startTime = new Date().getTime();
    timerInterval = setInterval(updateTimer, 1000); // Update the timer every second
}

// Function to stop the timer
function stopTimer() {
    clearInterval(timerInterval);
    updateTimer(); // Update the timer display one last time to ensure it shows the final time
}

// Function to reset the timer
function resetTimer() {
    stopTimer();
    document.getElementById("timer").innerText = 'Time: 00:00:00';
    document.getElementById("congratulationsMessage").style.display = "none";
    startTimer();
}

// Function to start a new puzzle
function newPuzzle() {
    resetTimer(); // Call the resetTimer function to reset the timer
    window.location.href = '/'; // Reload the page to trigger the Flask route for a new puzzle
}

// Call startTimer when the page loads
window.onload = startTimer;
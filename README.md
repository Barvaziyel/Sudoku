# Sudoku Web Application

Welcome to my personal project—a fully interactive **Sudoku puzzle generator and solver** web application. I built this as a fun way to dive deeper into web development using Flask and to challenge myself with game logic and UI design. Feel free to explore, play a game, or dive into the code!

## Features

- **Dynamic Puzzle Generation**: Enjoy new puzzles every time you play. No two games are the same!
- **Interactive Gameplay**: Input your guesses, try different strategies, and see if you can conquer Sudoku.
- **Solution Validation**: Stuck? Hit the "Check Solution" button to see if you're on the right track or use it to learn from your mistakes.
- **Timer**: Challenge yourself against the clock! See how quickly you can solve Sudoku puzzles.
- **Adaptive Design**: Play comfortably on any device, thanks to responsive design elements.
- **Clear Board**: Easily reset your current progress on the puzzle without needing to refresh the entire page or start a new puzzle.
- **Get Hint**: Stuck on a tough spot? Use the "Get Hint" button to reveal a helpful hint for one of the unsolved cells.

## Built With

- **Flask**: Manages backend operations and serves up the interactive web pages.
- **HTML/CSS**: Creates and styles the layout for an engaging user experience.
- **JavaScript**: Powers the frontend logic, including the timer and validation functions.
- **canvas-confetti**: Because everyone loves a little celebration after solving a puzzle!

## Getting Started

Here’s how to get the app running on your local machine for some fun and exploration.

### Prerequisites

You'll need **Python 3** and **pip** installed on your computer. Virtual environments are recommended but optional.

### Setup

1. **Clone this repository**:
    ```bash
    git clone https://github.com/Barvaziyel/Sudoku.git

2. **Navigate to the project directory**:
    ```bash
    cd Sudoku

3. **Set up a virtual environment** (optional):
    ```bash
    python -m venv venv
    source venv/bin/activate # Unix/macOS
    venv\Scripts\activate # Windows

4. **Install the required packages**:
    ```bash
    pip install -r requirements.txt

5. **Fire up the server**:
    ```bash
    flask run

6. **Visit `http://127.0.0.1:5000/` in your browser** and start playing!

## How to Play

Simply fill in the grid with numbers following standard Sudoku rules. Use the buttons below the grid to:
- **Check My Solution**: Validates your current answers.
- **Show Solution**: Reveals the correct answers (no peeking!).
- **New Puzzle**: Loads a fresh Sudoku puzzle to tackle.
- **Clear Board**: Clears all entries you've made so far, allowing you to start filling out the puzzle again from scratch.
- **Get Hint**: Provides a hint by filling in a correct number in one of the empty cells.


## Fun Project Note

This was a personal project made just for fun and to improve my coding skills. It's not perfect, but it was a great learning experience. If you have suggestions for improvements or new features, feel free to fork this repo and experiment on your own!

## License

This project is open source and available under the [MIT License](LICENSE.txt).

## Acknowledgments

- Hat tip to anyone whose code was used as inspiration.
- Big thanks to the Flask and JavaScript communities for the amazing libraries and frameworks.
- And, of course, a shoutout to all the Sudoku enthusiasts out there! Keep solving those puzzles! 🧩
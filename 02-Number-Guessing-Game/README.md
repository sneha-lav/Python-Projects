# GuessMaster 🎯

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-success)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

A command-line number guessing game built with Python where players try to guess a randomly generated number within a limited number of attempts. The game offers multiple difficulty levels, helpful hints, and performance feedback to make the experience more engaging.

---

## Features

- Multiple difficulty levels
- Random number generation
- Limited attempts
- Too High / Too Low hints
- Warm & Cold hint system
- Score based on attempts
- Replay option
- Modular code organization

---

## Concepts Practiced

- Variables
- Data Types
- Conditional Statements
- Loops
- Functions
- Random Module
- User Input
- Modular Programming

---

## Project Structure

```text
02-Number-Guessing-Game/
│
├── main.py
├── game.py
└── README.md
```

---

## How to Run

Navigate to the project folder.

```bash
cd 02-Number-Guessing-Game
```

Run the project.

```bash
py main.py
```

---

## Sample Output

```text
=====================================
        🎯 GUESSMASTER 🎯
=====================================

Choose Difficulty

1. Easy
2. Medium
3. Hard

> 2

Guess the number between 1 and 100

Attempt 1/7

> 65

⬆️ Too High
🌡️ You're Close!

Attempts Left: 6
```

---

## Learning Outcomes

Through this project I practiced:

- Generating random numbers
- Designing game logic
- Creating reusable functions
- Handling user input
- Writing modular Python programs

---

## Future Improvements

### v1.1
- [ ] Store and display the highest score
- [ ] Allow players to choose a custom number range
- [ ] Improve input validation

### v1.2
- [ ] Add player statistics
- [ ] Add multiple game modes

### v1.3
- [ ] Save game history to a file
- [ ] Display a leaderboard

### v1.4
- [ ] Add colored terminal output using `colorama`
- [ ] Introduce a timed challenge mode

### v2.0
- [ ] Develop a graphical user interface (GUI) using Tkinter

---

## Credits

Inspired by the **21 Python Projects** series by **Tech With Tim**.
# Python Wordle

A command-line Wordle clone written in Python.  
This version retrieves words from the WordGameDB API, validates user input, and provides colorized feedback using Wordle-style rules.
This project uses the WordGameDB.com API for educational and non-commercial purposes.


## Features

- Fetches a random word from an external API  (WordGameDB)
- ANSI color-coded output for terminal play
- Two-pass Wordle evaluation algorithm:
  - Green: correct letter in the correct position
  - Yellow: correct letter in the wrong position
  - Gray: incorrect letter
- Input validation (alphabetic only, correct word length)
- Dynamic guess count based on word length
- Ability to replay multiple rounds

## Requirements

- Python 3.7+
- `requests` library

Install dependencies:
```bash
pip install requests
```
## How to Run

Clone the repository:
git clone https://github.com/JacobOlds/python-wordle.git

Change into the project directory:
cd python-wordle

Install dependencies:
pip install requests

Run the game:
python Wordle.py

# Yatzy Game

A Python implementation of the Yatzy dice game with unit tests.

## Installation
Clone the repository:
git clone https://github.com/JadeGreen42/Yatzy-Game.git
cd Yatzy-Game

## How to Run
python main.py

## How to Play

The game follows standard Yatzy rules.

1. The game consists of multiple rounds.
2. In each round, five dice are rolled.
3. The player may re-roll dice up to two additional times.
4. After the final roll, a scoring category must be selected.
5. The game ends after all scoring categories are filled.

When prompted:
- Enter the numbers (1–5) of the dice you want to keep.
- Press Enter without input to reroll all dice.

Example:
If you want to keep dice 1 and 3, enter:
13

## Running Tests
pytest

## Project Structure
logic.py      → dice logic  
scoring.py    → scoring rules  
game.py       → game flow  
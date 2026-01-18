# Snake Game - Python Turtle

## Description

Creating the Snake Game with **Python** was an **absolutely exciting** experience. It taught me a lot about **OOP** and core programming concepts.

This is my first project where I applied **inheritance**, one of the major concepts of Object-Oriented Programming. I also organized my code into four distinct files to keep it clean, readable, and maintainable:

- `main.py`: The entry point of the game.
- `snake.py`: Handles snake movement and body logic.
- `food.py`: Manages random food generation and types.
- `score.py`: Controls the scoreboard and game-over logic.

## Features

### 💀 Lose Logic:

- **Wall Collision:** If the snake hits any of the four walls, the game ends.
- **Self Collision:** If the snake's head touches any part of its body, it's Game Over.

### 🍎 Score & Growth Logic:

- **Food Types:** - Small food = 1 point.
  - Big food = 3 points.
- **Dynamic Difficulty:** Every time the snake eats, its **length increases** and its **speed gets faster**.

## Controls

Use the arrow keys to control the snake:

- ⬆️ **Up**
- ⬇️ **Down**
- ⬅️ **Left**
- ➡️ **Right**

## How to Test

1. **Executable:** You can download the executable file here: [SNAKE_GAME.EXE](https://drive.google.com/file/d/1eXZoffdaONJgkMlchRyt3yXpQN08T7ZB/view?usp=drive_link)
2. **Run from Source:** - Ensure you have Python installed.
   - Clone this repository.
   - Run the following command:
   ```bash
   python main.py
   ```

## Gallery

![starting the game](image.png)

![the snake gets longer after eating](image-1.png)

![The game is over when the snake collids with walls](image-2.png)

![The game is over when the snake collids with itself](image-3.png)

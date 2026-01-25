# Snake Game - Python (OOP & Turtle Graphics)

## Description
Creating the Snake Game was a milestone in my programming journey. This project served as a deep dive into **Object-Oriented Programming (OOP)** principles, specifically focusing on clean code and modularity.

This is my first project implementing **Inheritance**, which allowed for a more scalable and organized codebase. The project is split into two versions to experiment with different game mechanics.

## Project Structure
The repository is organized into four main modules:
- `main.py`: The entry point and game loop.
- `snake.py`: Logic for snake movement and body segment management.
- `food.py`: Handles random food spawning and distinct food types.
- `score.py`: Manages the real-time scoreboard and high-score logic.

## Game Modes
I have developed two distinct versions of the game:
1. **Collision Mode:** Classic difficulty where hitting a wall results in an immediate Game Over.
2. **Screen-Wrap Mode:** A modern twist where the snake can pass through walls and reappear on the opposite side.

## Features
### 🍎 Scoring & Mechanics
- **Dynamic Food Types:** - Small Food: +1 Point.
  - Big Food: +3 Points.
- **Progressive Difficulty:** The snake's **speed increases** and its **length grows** every time it eats.

### 💀 Game Over Conditions
- **Self-Collision:** Touching any part of the snake's own body.
- **Wall Collision:** (Only in the Collision Version).

## How to Run

### 1. Executables
Download and play directly:
- [SNAKE_GAME_Collision_Mode.exe](https://drive.google.com/file/d/1eXZoffdaONJgkMlchRyt3yXpQN08T7ZB/view?usp=drive_link)
- [SNAKE_GAME_Screen_Wrap_Mode.exe](https://drive.google.com/file/d/10scYCkE1rq6ydxFmqbenQNGam5t0TfO7/view?usp=drive_link)

### 2. From Source
Ensure you have Python installed, then:
```bash
# Clone the repository
git clone [https://github.com/YourUsername/YourRepoName](https://github.com/YourUsername/YourRepoName)

# Navigate to your preferred version
cd "Collision Version"  # or cd "Screen-Wrap Version"

# Run the game
python main.py

Gallery:
![alt text](image-4.png) ![alt text](image-1-1.png) ![alt text](image-2-1.png) ![alt text](image-3-1.png)
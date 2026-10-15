# 🏓 Pong — Python & Pygame

A classic two-player Pong game developed using **Python** and **Pygame**, featuring real-time paddle movement, ball physics, collision detection, and a competitive scoring system.

This project demonstrates fundamental software development concepts, including **object-oriented programming (OOP), event-driven programming, game loops, and collision handling**.

## Features

- **Local Two-Player Gameplay** — Compete against another player using separate keyboard controls.
- **Responsive Paddle Movement** — Smooth movement with boundary restrictions to keep paddles within the game window.
- **Ball Collision Detection** — The ball rebounds when colliding with paddles or the top and bottom walls.
- **Dynamic Ball Trajectories** — The ball's vertical direction changes depending on where it strikes a paddle.
- **Real-Time Score Tracking** — Both players' scores are displayed throughout the match.
- **Win Condition** — The first player to reach 10 points wins.
- **Automatic Game Reset** — After displaying the winner, the game resets for another match.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language and game logic |
| Pygame | Graphics rendering, keyboard input, and collision handling |
| Object-Oriented Programming | Encapsulation of paddle and ball behaviour |

## Getting Started

### Prerequisites

Ensure that Python 3 and pip are installed on your computer.

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/SalehSandhu/Pong.git
```

**2. Navigate to the project directory**

```bash
cd Pong
```

**3. Install Pygame**

```bash
python -m pip install pygame
```

**4. Run the game**

Navigate to the folder containing the Python game script and execute:

```bash
python <game_filename>.py
```

Replace `<game_filename>` with the actual name of your Python file.

## Controls

| Action | Left Player | Right Player |
|---|---|---|
| Move Up | W | ↑ Up Arrow |
| Move Down | S | ↓ Down Arrow |

Both players control their paddles simultaneously. The objective is to prevent the ball from passing their paddle while attempting to score against their opponent.

**Winning condition:** The first player to score 10 points wins the match.

## How It Works

### Object-Oriented Design

The game uses two primary classes to manage its interactive components.

**Paddle Class**

The `Paddle` class manages each player's paddle, including:

- Position and dimensions
- Vertical movement and movement speed
- Rendering the paddle on screen
- Resetting its position after a match

**Ball Class**

The `Ball` class manages the ball's behaviour, including:

- Horizontal and vertical velocity
- Position updates during gameplay
- Rendering the ball
- Resetting its position and reversing its horizontal direction

### Collision Detection

Collision detection determines how the ball interacts with the game environment.

When the ball reaches the top or bottom boundary, its vertical velocity is reversed:

```python
ball.y_vel *= -1
```

When the ball collides with a paddle, its horizontal velocity is reversed. Its vertical velocity is then calculated based on the distance between the collision point and the paddle's centre.

This allows players to influence the ball's trajectory through paddle positioning.

### Game Loop

The game operates at a target of **60 frames per second (FPS)**.

Each iteration of the main loop:

1. Processes game events and keyboard input.
2. Updates paddle positions based on player input.
3. Updates the ball's position using its velocity.
4. Detects and handles collisions.
5. Checks whether either player has scored.
6. Evaluates the winning condition.
7. Renders the updated game state.

The game uses `pygame.time.Clock()` to regulate the frame rate and maintain consistent gameplay.

## What I Learned

Developing this project helped reinforce several important programming concepts:

- **Object-Oriented Programming:** Using classes, constructors, attributes, and methods to organise game components.
- **Event-Driven Programming:** Processing keyboard inputs and window events through Pygame.
- **Game State Management:** Tracking player scores, ball positions, and match outcomes.
- **Collision Detection:** Implementing coordinate-based collision checks and velocity calculations.
- **Code Organisation:** Separating rendering, movement, collision detection, and game logic into reusable functions.

## 🔮 Future Improvements

Potential enhancements include:

- [ ] Single-player mode with an AI-controlled opponent
- [ ] Start and pause menus
- [ ] Adjustable difficulty settings
- [ ] Sound effects for paddle collisions and scoring
- [ ] Progressive ball speed increases
- [ ] Improved collision handling near paddle edges

## Author

**Saleh Sandhu**

- GitHub: [@SalehSandhu](https://github.com/SalehSandhu)

---

*Developed using Python and Pygame as a practical project to strengthen software engineering and game development fundamentals.*

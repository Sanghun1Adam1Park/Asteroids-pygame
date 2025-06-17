# Asteroids-pygame

A classic arcade-style asteroids game built with Python and Pygame. This project was created as a fun way to learn the fundamentals of game development.

![Gameplay Screenshot](<ingame.png>)

## Table of Contents

- [About The Project](#about-the-project)
- [Key Features](#key-features)
- [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [How to Play](#how-to-play)
- [Roadmap](#roadmap)
- [Acknowledgments](#acknowledgments)

## About The Project

This is a clone of the classic Atari game "Asteroids." The player controls a spaceship in an asteroid field and must shoot and destroy asteroids while avoiding collisions. When an asteroid is shot, it breaks into smaller pieces, increasing the challenge. The game features a classic "wrap-around" screen, where objects that fly off one edge of the screen reappear on the opposite edge.

## Key Features

* **Player-Controlled Spaceship:** Full control over thrust and rotation.
* **Shoot & Destroy:** Fire bullets to destroy asteroids.
* **Splitting Asteroids:** Large asteroids break into smaller, faster pieces when shot.
* **Screen Wrapping:** Seamlessly travel off one side of the screen and reappear on the other.
* **Collision Detection:** Game ends if the ship collides with an asteroid.
* **Scoring System:** Earn points for every asteroid destroyed.

## Built With

This project was built using the following technologies:

* [Python 3](https://www.python.org/)
* [Pygame](https://www.pygame.org/news)

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

Make sure you have Python 3 and pip installed on your system.

* **Python 3**
    ```sh
    python --version
    ```
* **pip**
    ```sh
    pip --version
    ```

### Installation

1.  **Clone the repository**
    ```sh
    git clone [https://github.com/your_username/your_repository_name.git](https://github.com/your_username/your_repository_name.git)
    ```
2.  **Navigate to the project directory**
    ```sh
    cd your_repository_name
    ```
3.  **Install the required packages**
    This project uses Pygame. You can install it using pip.
    ```sh
    pip install -r requirements.txt
    ```
    *(Note: If you don't have a `requirements.txt` file, you can create one with `pip freeze > requirements.txt` after installing pygame, or just instruct users to run `pip install pygame`)*

## How to Play

Once the game is running, use the following controls to play:

* **Rotate Ship:** `LEFT` and `RIGHT` Arrow Keys
* **Thrust Forward:** `UP` Arrow Key
* **Shoot:** `SPACEBAR`

The goal is to survive as long as possible!

## Roadmap

This is a list of proposed features and improvements for future versions of the game. 

### Core Gameplay & Mechanics
- [ ] **Scoring System:** Implement a system to award points for destroying asteroids.
- [ ] **Multiple Lives & Respawning:** Give the player multiple lives and a respawn mechanic, perhaps with temporary invincibility.
- [ ] **Screen Wrapping:** Make all game objects (ship, asteroids, bullets) wrap around the screen edges instead of disappearing.
- [ ] **Lumpy Asteroids:** Change the asteroid generation to create more natural, irregular polygon shapes instead of perfect circles.
- [ ] **Triangular Ship Hitbox:** Implement a more precise, polygon-based hitbox for the player's ship instead of a simple circle.

### Player Movement & Abilities
- [ ] **Player Acceleration:** Refine the player movement to include acceleration and deceleration for a more realistic "space flight" feel, rather than instant movement.
- [ ] **Bombs:** Add a secondary weapon system allowing the player to drop powerful, area-of-effect bombs.

### Power-ups & Weapons
- [ ] **Shield Power-up:** A collectible item that grants the player temporary invincibility.
- [ ] **Speed Power-up:** A collectible item that temporarily increases the ship's maximum speed or thrust.
- [ ] **Different Weapon Types:** Implement new weapons, such as a spread-shot or a laser beam, that the player can collect or switch to.

### Visuals & Effects
- [ ] **Explosion Effects:** Add a particle-based explosion animation when asteroids are destroyed.
- [ ] **Background Image:** Add a scrolling or static space-themed background image to replace the solid color.

## Acknowledgments

A list of resources that you found helpful.
* [Pygame Documentation](https://www.pygame.org/docs/)
* [Boot.dev - Backend dev Tutorial](https://boot.dev/)

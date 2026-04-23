# Air Raid – 2D Shooter Game (Python, Pygame)

## Overview

Air Raid is a real-time 2D shooter built using Python and Pygame.
The player controls a ship, fights a boss enemy, and uses power-ups to survive and win.

## Features

* Real-time movement and shooting system
* Boss enemy with dynamic attack patterns
* Power-ups:

  * Health regeneration
  * Rapid-fire boost
  * Triple-shot attack
* Multiple game states:

  * Menu
  * Instructions
  * Gameplay
  * Win / Loss screens
* Sound effects and background music

## Controls

* **W / A / S / D** → Move
* **Enter** → Shoot

## Installation

Make sure Python is installed, then install dependencies:

```
pip install pygame
```

## How to Run

From the project folder:

```
python AirRaid.py
```

## Project Structure

```
AirRaid.py        # Main game loop
player.py         # Player (Peaship)
enemy.py          # Boss (Zomboss)
projectiles.py    # Bullets and fireballs
powerups.py       # Health and boost systems
assets.py         # Image loading
assets/           # Images and sounds
```

## Technologies Used

* Python
* Pygame

## Notes

This project was originally created and later refactored to improve structure, modularity, and maintainability.

## Future Improvements

* Improved enemy AI
* Additional levels or enemies
* Visual effects for power-ups and hits
* Score system

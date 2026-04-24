# Air Raid – 2D Shooter Game (Python, Pygame)

## Demo

![Gameplay Demo](demo.gif)

---

## Overview

Air Raid is a real-time 2D shooter built using Python and Pygame. The player controls a ship, battles a boss enemy, and uses power-ups to survive and win. The project focuses on game loop design, object-oriented programming, and modular code structure.

---

## Features

* Real-time movement and shooting system
* Boss enemy with dynamic attack patterns
* Power-up system:

  * Health regeneration
  * Rapid-fire boost
  * Triple-shot attack
* Multiple game states:

  * Menu
  * Instructions
  * Gameplay
  * Win / Loss screens
* Sound effects and background music
* Organized modular code (separate files for enemies, projectiles, UI, etc.)

---

## Controls

* **W / A / S / D** → Move
* **Enter** → Shoot

---

## How to Run

### 1. Install dependencies

```bash
pip install pygame
```

### 2. Run the game

```bash
python AirRaid.py
```

---

## Project Structure

```bash
AirRaid.py          # Main game loop
assets.py           # Image and sound loading
enemy.py            # Enemy (boss) logic
powerups.py         # Power-up system
projectiles.py      # Projectile behavior
settings.py         # Game settings/constants
ui.py               # UI elements (buttons, screens)
user.py             # Player logic
assets/             # Images, audio, and game assets
```

---

## Technologies Used

* Python
* Pygame

---

## What I Learned

* Structuring larger Python projects using multiple modules
* Implementing a real-time game loop
* Handling collisions and sprite groups in Pygame
* Managing assets (images, audio) efficiently
* Using Git and GitHub for version control

---

## Future Improvements

* Improved enemy AI and additional enemy types
* More power-ups and gameplay mechanics
* Better animations and visual effects
* Menu polish and UI enhancements

---

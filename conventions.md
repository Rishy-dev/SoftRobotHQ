# Coding and Project Conventions for Soft Robot HQ

This document defines coding conventions and project structure guidelines to maintain consistency across the Soft Robot HQ simulation project.

## File and Folder Structure

* **main.py** – Entry point of the simulation.
* **player.py** – CEO character class and movement logic.
* **robot.py** – Soft robot behavior and task simulation.
* **privacy.py** – Privacy system logic.
* **building.py** – Environment, building, and room layout.
* **utils.py** – Helper functions, if needed.

**Naming Convention:**

* Files use `snake_case.py`.
* Classes use `PascalCase`.
* Variables and functions use `snake_case`.
* Constants use `UPPER_CASE`.

## Coding Style

* Use 4 spaces for indentation.
* Max line length: 80 characters.
* Use meaningful variable and function names.
* Include docstrings for all classes and methods.
* Separate classes and major functions into different files/modules.

## Function and Class Conventions

* **Player class:** Handles CEO movement and input.
* **SoftRobot class:** Handles robot movement, task simulation, and data collection.
* **PrivacySystem class:** Calculates privacy weakness and growth.
* **Room/Building classes:** Defines environment structure.

**Update Methods:**

* All dynamic changes (movement, privacy growth, robot animation) should be in `update()` methods.
* `update()` functions should run every frame to simulate real-time behavior.

## General Guidelines

* Avoid hardcoding magic numbers; use constants when possible.
* Keep modules focused on single responsibilities.
* Document any changes and extensions in the README.md.
* Use comments for complex logic or mathematical operations.

## Versioning

* Follow semantic versioning (e.g., v1.0.0).
* Update the README and Conventions.md when adding features or changing structure.

## Example Usage

```python
from player import Player
player = Player(position=(0,1,0))
player.update()
```

## License

Apache 2.0 License


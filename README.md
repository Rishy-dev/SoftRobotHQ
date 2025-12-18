# Soft Robot HQ Simulation

## Overview

Soft Robot HQ is a modular Python 3D simulation where you play as the CEO of a company utilizing soft robots. The simulation allows you to explore a multi-floor building where robots perform tasks for humans, while tracking privacy weaknesses over time.

The project is built using the [Ursina Engine](https://www.ursinaengine.org/) for Python, providing a simple yet interactive 3D environment.

## Features

* **Multi-floor building:** Lobby, manufacturing floor, CEO office, and control room.
* **CEO character:** Walk around the building using WASD keys.
* **Soft robots:** Robots perform tasks with organic motion (squash and stretch effect).
* **Privacy system:** Simulates weakening of privacy over time and visualizes it in the lobby.
* **Modular structure:** Code is split into separate files for easy extension.

## Folder Structure

```
SoftRobotHQ/
│
├─ main.py          # Starts the simulation, sets up the world
├─ player.py        # CEO character movement
├─ robot.py         # Soft robot behavior
├─ privacy.py       # Privacy weakness simulation
├─ building.py      # Building layout & environment
├─ utils.py         # Helper functions (optional)
```

## Controls

* `W` – Move forward
* `S` – Move backward
* `A` – Move left
* `D` – Move right

## Installation

1. Install Python 3.8+ ([https://www.python.org/](https://www.python.org/))
2. Install Ursina Engine:

   ```bash
   pip install ursina
   ```
3. Clone or download the project repository.

## Running the Simulation

```bash
python main.py
```

* Your character will spawn in the lobby.
* Walk around the building to observe robots.
* The console prints the **current privacy weakness**.

## Extending the Simulation

* Add interactive **CEO decision panels** to change robot behavior or privacy growth.
* Add **robot-human interaction logic**.
* Improve visuals with **post-processing effects** to reflect privacy and ethical states.
* Add UI to display **Privacy Weakness Meter** or robot task progress.

## License

Apache 2.0 License

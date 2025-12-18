# Soft Robot HQ - Python Dependencies

This file lists all Python packages required to run the Soft Robot HQ simulation.

## Installation

Run the following command to install all dependencies:

```bash
pip install -r requirements/base.txt -r requirements/dev.txt -r requirements/optional.txt
```

## Requirements

```
ursina>=3.0.1
```

> Note: Ursina automatically handles Panda3D as a dependency.

## Optional (for development / testing)

```
pillow>=10.0.0   # for image handling if needed
numpy>=1.26.0    # for math or array operations
```

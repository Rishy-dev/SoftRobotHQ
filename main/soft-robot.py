from ursina import *
import math

class SoftRobot(Entity):
    def __init__(self, position=(0,0,0), task="Idle", **kwargs):
        super().__init__()
        self.model = 'cube'
        self.color = color.orange
        self.scale_y = 1.5
        self.position = position
        self.flex_intensity = 0.2
        self.data_collected = 0
        self.task = task

        for key, value in kwargs.items():
            setattr(self, key, value)

    def update(self):
        # Soft motion (squash/stretch)
        self.scale_y = 1.5 + math.sin(time.time()) * self.flex_intensity
        # Simulate performing a task
        self.data_collected += 0.01 * time.dt

from ursina import *

class Player(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.model = 'cube'
        self.color = color.azure
        self.scale_y = 2
        self.collider = 'box'
        self.speed = 5

        for key, value in kwargs.items():
            setattr(self, key, value)

    def update(self):
        move = Vec3(
            held_keys['d'] - held_keys['a'],
            0,
            held_keys['w'] - held_keys['s']
        )
        self.position += move * time.dt * self.speed

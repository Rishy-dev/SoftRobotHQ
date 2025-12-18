from ursina import *

class Building:
    def __init__(self):
        # Simple floors and walls
        self.floor = Entity(model='plane', scale=(20,1,20), color=color.light_gray)
        self.lobby = Entity(model='cube', scale=(10,5,10), color=color.white, position=(0,2.5,0))

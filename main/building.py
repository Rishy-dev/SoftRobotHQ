from ursina import *

class Room(Entity):
    def __init__(self, position=(0,0,0), size=(5,5,5), color_val=color.light_gray):
        super().__init__()
        self.model = 'cube'
        self.color = color_val
        self.scale = Vec3(*size)
        self.position = Vec3(*position)
        self.collider = 'box'

class Building:
    def __init__(self):
        # Floors
        self.rooms = []
        # Lobby
        self.rooms.append(Room(position=(0,2.5,0), size=(10,5,10), color_val=color.white))
        # Manufacturing floor
        self.rooms.append(Room(position=(0,7.5,0), size=(15,5,15), color_val=color.gray))
        # CEO office
        self.rooms.append(Room(position=(0,12.5,0), size=(8,5,8), color_val=color.cyan))
        # Data/control room
        self.rooms.append(Room(position=(12,12.5,0), size=(6,5,8), color_val=color.red))

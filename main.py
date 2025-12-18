from ursina import *
from player import Player
from robot import SoftRobot
from privacy import PrivacySystem
from building import Building

app = Ursina()

# Create world
building = Building()
player = Player(position=(0,1,0))
robots = [SoftRobot(position=(x,0, z)) for x in range(-5,6,5) for z in range(-5,6,5)]
privacy = PrivacySystem()

def update():
    player.update()
    for r in robots:
        r.update()
    privacy.update()
    # Optional: print privacy level
    print(f'Privacy Weakness: {privacy.weakness:.2f}')

app.run()

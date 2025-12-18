from ursina import *
from player import Player
from robot import SoftRobot
from privacy import PrivacySystem
from building import Building

app = Ursina()

# World setup
building = Building()
player = Player(position=(0,1,0))

# Create soft robots
robots = []
for x in range(-5,6,5):
    for z in range(-5,6,5):
        robots.append(SoftRobot(position=(x,1,z), task="Assembling"))

# Privacy system
privacy = PrivacySystem()

# Floor navigation
camera.y = 5
camera.rotation_x = -30

def update():
    player.update()
    for r in robots:
        r.update()
    privacy.update(robots)

    # Visualize privacy: lobby brightness decreases as privacy weakens
    lobby = building.rooms[0]
    lobby.color = color.rgb(255, max(0, 255-int(privacy.weakness*2.5)), max(0, 255-int(privacy.weakness*2.5)))

    # Optional: print status
    print(f'Privacy Weakness: {privacy.weakness:.2f}')

app.run()

import time

class PrivacySystem:
    def __init__(self):
        self.weakness = 10  # 0 = secure, 100 = very weak
        self.growth_rate = 0.3

    def update(self, robots):
        # Increase based on number of robots and their data collection
        robot_factor = sum([r.data_collected for r in robots])
        self.weakness += self.growth_rate * time.dt + robot_factor * 0.1
        if self.weakness > 100:
            self.weakness = 100

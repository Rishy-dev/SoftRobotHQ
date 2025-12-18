class PrivacySystem:
    def __init__(self):
        self.weakness = 10  # 0 = secure, 100 = very weak
        self.growth_rate = 0.5

    def update(self):
        self.weakness += self.growth_rate * time.dt
        if self.weakness > 100:
            self.weakness = 100

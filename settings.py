class Settings:
    """store all the settings in aline invasion"""

    def __init__(self):
        """initialize all the static setting"""
        # screen setting
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship setting
        self.ship_speed = 1
        self.ship_limits = 2

        # bullet setting
        self.bullet_speed = 1.0
        self.bullet_width = 500
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        self.bullet_allowed = 20

        # alien setting
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction 1:right, -1:left
        self.fleet_direction = 1

        # speed up game
        self.speedup_scale = 1.1
        # speed up score
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 1
        self.alien_speed = 1.0

        # fleet direction
        self.fleet_direction = 1

        #score
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.bullet_speed
        self.alien_speed *= self.alien_speed

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
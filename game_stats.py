class GameStats:
    """game statistic"""

    def __init__(self, ai_game):
        """initial"""
        self.settings = ai_game.settings
        self.reset_stats()
        # when game starts, it is active
        self.game_active = True

    def reset_stats(self):
        """initialize the information which may change during the game"""
        self.ships_left = self.settings.ship_limits
        self.aliens_killed = 0
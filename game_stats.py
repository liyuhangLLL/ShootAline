class GameStats:
    """game statistic"""

    def __init__(self, ai_game):
        """initial"""
        self.settings = ai_game.settings
        self.reset_stats()
        # when game starts, it is active
        self.game_active = False

        # highest score
        try:
            with open('data/high_score.txt', 'r') as f:
                self.high_score = int(f.read().rstrip())
        except FileNotFoundError:
            pass
        else:
            self.high_score = 0

    def reset_stats(self):
        """initialize the information which may change during the game"""
        self.ships_left = self.settings.ship_limits
        self.score = 0
        self.level = 1
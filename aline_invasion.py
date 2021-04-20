import sys
import pygame
from settings import Settings
from ship import Ship

class AlineInvasion:
    """manager game source and class behaviours"""

    def __init__(self):
        """initial game and create the source"""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Aline Invasion')

        self.ship = Ship(self)

    def run_game(self):
        """start main loop"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        # response the events of keyboard and mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            # right move the ship
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_LSHIFT:
            self.ship.speed_up = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_LSHIFT:
            self.ship.speed_up = False

    def _update_screen(self):
        # redraw the screen in every loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # make new plot screen visible
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlineInvasion()
    ai.run_game()
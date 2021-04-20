import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Aline class"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # load aline image and set rect attribution
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        width, height = self.rect.size

        # set each aline to the left top of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the accurate position of each aline
        self.x = float(self.rect.x)

    def update(self):
        """rigth move aliens"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """if alien is located at the edge, return TRUE"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left < 0:
            return True

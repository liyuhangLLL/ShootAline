import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Aline class"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        # load aline image and set rect attribution
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # set each aline to the left top of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the accurate position of each aline
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
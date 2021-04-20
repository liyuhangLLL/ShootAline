import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    # manager the bullet

    def __init__(self, ai_game):
        """build a bullet"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0,
                                self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # store the position of the bullet
        self.y = float(self.rect.y)

    def update(self):
        """move up the bullet"""
        self.y -= self.settings.bullet_speed
        # updated bullet position
        self.rect.y = self.y

    def draw_bullet(self):
        """draw the bullet"""
        pygame.draw.rect(self.screen, self.color, self.rect)
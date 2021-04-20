import sys
import pygame


class AlineInvasion:
    """manager game source and class behaviours"""

    def __init__(self):
        """initial game and create the source"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Aline Invasion')

    def run_game(self):
        """start main loop"""
        while True:
            # supervise the events of keyboard and mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # make new plot screen visible
            pygame.display.flip()


if __name__ == '__main__':
    ai = AlineInvasion()
    ai.run_game()
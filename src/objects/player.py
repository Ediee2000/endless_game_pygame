from ..utils import *
import pygame


class Player:
    """
    Class to manage player information.
    """

    name: str
    classe: str
    level: int

    def __init__(self, name, classe):
        """
        Initialize a Player object.

        Args:
            name (str): The name of the player.
            classe (str): The class of the player.
        """
        self.name = name
        self.classe = classe
        self.level = 1

    def draw(self, x, y, screen: pygame.Surface):
        """
        Draw a stickman on the screen.

        Args:
            x (int): The x-coordinate of the stickman's position.
            y (int): The y-coordinate of the stickman's position.
            screen (pygame.Surface): The surface to draw on.
        """
        pygame.draw.circle(screen, BLACK, (x, y - 5), 5)
        pygame.draw.line(screen, RED, (x - 5, y + 2), (x + 5, y + 2), 5)
        pygame.draw.line(screen, BLUE, (x, y + 5), (x - 5, y + 15), 5)
        pygame.draw.line(screen, BLUE, (x, y + 5), (x + 5, y + 15), 5)

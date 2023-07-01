import pygame
from .tiles import Hexagon
from ..utils import *

class Mapa:
    """A class responsible for storing information about the map."""

    def __init__(self):
        """Initialize a new Mapa object."""
        self.hexagons = []

    def add_hexagon(self, hexagon: Hexagon):
        """Adds a new hexagon to the map.

        Args:
            hexagon (Hexagon): The hexagon to add.
        """
        self.hexagons.append(hexagon)

    def check_collision(self, x, y):
        """Check if coordinates collide with any hexagon on the map.

        Args:
            x (int): The x-coordinate to check.
            y (int): The y-coordinate to check.

        Returns:
            bool: True if collision occurred, False otherwise.
        """
        for hexagon in self.hexagons:
            if hexagon.rect.collidepoint(x, y):
                return True
        return False

    def get_hexagon(self, x, y):
        """Get the hexagon at the specified coordinates, if any.

        Args:
            x (int): The x-coordinate to check.
            y (int): The y-coordinate to check.

        Returns:
            Hexagon|None: The hexagon at the specified coordinates, or None if no hexagon is found.
        """
        for hexagon in self.hexagons:
            if hexagon.rect.collidepoint(x, y):
                return hexagon
        return None

    def realign_hexagons(self, new_center: Hexagon):
        """Recalculate the coordinates of all hexagons and move them to the center of the screen.

        Args:
            new_center (Hexagon): The new center hexagon.
        """
        center_x = (SCREEN_WIDTH + PANEL_WIDTH) // 2
        center_y = SCREEN_HEIGHT // 2
        dx = center_x - new_center.x
        dy = center_y - new_center.y

        for hexagon in self.hexagons:
            hexagon.x += dx
            hexagon.y += dy
            hexagon.rect = pygame.Rect(hexagon.x - RADIUS, hexagon.y - RADIUS, 2 * RADIUS, 2 * RADIUS)
            hexagon.calculate_points()

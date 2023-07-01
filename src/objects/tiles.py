import pygame
import math
import random

from ..utils import *

class Hexagon:
    """A class to store information about hexagons on a map."""

    def __init__(self, x, y, radius, color, category=None):
        """Initialize a new Hexagon object.

        Args:
            x (int): The x-coordinate of the hexagon.
            y (int): The y-coordinate of the hexagon.
            radius (int): The radius of the hexagon.
            color (tuple[int, int, int]): The color of the hexagon represented as an RGB tuple.
            category (str, optional): The category of the hexagon. Defaults to None.
        """
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.category = category
        self.adjacent_hexagons = []
        self.points = []
        self.rect = pygame.Rect(x - radius, y - radius, 2 * radius, 2 * radius)
        self.points = self.calculate_points()

    def __repr__(self):
        """Return a string representation of the Hexagon object."""
        return f"Tile: {self.x}, {self.y}, Category: {self.category}"

    def draw(self, screen):
        """Draw the hexagon on the screen.

        Args:
            screen (pygame.Surface): The surface to draw the hexagon on.
        """
        pygame.draw.polygon(screen, self.color, self.points)

    def calculate_points(self):
        """Calculate the coordinates of the points that define the hexagon.

        Returns:
            list[tuple[int, int]]: The coordinates of the points that define the hexagon.
        """
        points = []
        for i in range(6):
            angle_deg = 60 * i + 30
            angle_rad = math.radians(angle_deg)
            point_x = self.x + self.radius * math.cos(angle_rad)
            point_y = self.y + self.radius * math.sin(angle_rad)
            points.append((point_x, point_y))
        self.points = points
        return points

    def create_adjacent_hexagon(self, direction, mapa):
        """Create an adjacent hexagon in the specified direction.

        Args:
            direction (int): The direction of the adjacent hexagon (0-5).
            mapa (Mapa): The map object.

        Returns:
            Hexagon|None: The newly created adjacent hexagon or None if collision occurred.
        """
        angle_deg = 60 * direction
        angle_rad = math.radians(angle_deg)
        new_x = self.x + (1.8 * self.radius + DISTANCE) * math.cos(angle_rad)
        new_y = self.y + (1.8 * self.radius + DISTANCE) * math.sin(angle_rad)

        if mapa.check_collision(new_x, new_y):
            print("collision")
            self.adjacent_hexagons.append(mapa.get_hexagon(new_x, new_y))
            return None

        hexagon = Hexagon(new_x, new_y, self.radius, GRAY)
        self.adjacent_hexagons.append(hexagon)
        return hexagon
    
    def discover(self, mapa):
        """Discover a new hexagon by randomly assigning a category and adding adjacent hexagons.

        Args:
            mapa (Mapa): The map object.
        """
        if self.category is None:
            categories = [("Field", GREEN), ("Forest", DARK_GREEN), ("Lake", LIGHT_BLUE), ("Road", LIGHT_GRAY)]
            weights = [0.35, 0.35, 0.2, 0.1]
            choice = random.choices(categories, weights)[0]
            self.category = choice[0]
            self.color = choice[1]
            for direction in range(6):
                new_hex = self.create_adjacent_hexagon(direction, mapa)
                if new_hex is not None:
                    mapa.add_hexagon(new_hex)

    def isin_adjacent(self, hexagon):
        """Check if a given hexagon is adjacent to the current hexagon.

        Args:
            hexagon (Hexagon): The hexagon to check adjacency with.

        Returns:
            bool: True if the hexagon is adjacent, False otherwise.
        """
        return hexagon in self.adjacent_hexagons

import pygame
import random

class SourceImages:

    def __init__(self):
        """
        TODO
        Class to get sprites of hexagons
        """
    
        self.image = pygame.image.load("src\imgs\Hex_v01_grid.png")

    # Define the size of each tile
        tile_width = self.image.get_width() // 9
        tile_height = self.image.get_height() // 12

        self.tiles = []
        for row in range(12):
            for col in range(9):
                # Calculate the coordinates of the current tile
                left = col * tile_width
                upper = row * tile_height
                tile_rect = pygame.Rect(left, upper, tile_width, tile_height)

                # Extract the tile surface from the image
                tile_surface = self.image.subsurface(tile_rect)

                # Add the tile surface to the list
                self.tiles.append(tile_surface)
    @property
    def FIELD(self):
        """
        return pygame.Surface correspond of FIELD type but random
        """
        return random.choice([self.tiles[3 + (i * 9)] for i in range(1,6)])
    @property
    def FLORES(self):
        """
        return pygame.Surface correspond of FLORES type but random
        """
        return random.choice([self.tiles[2 + (i * 9)] for i in range(1,6)])
    @property
    def ROAD(self):
        """
        return pygame.Surface correspond of ROAD type but random
        """
        return random.choice([self.tiles[0 + (i * 9)] for i in range(1,6)])
    @property
    def LAKE(self):
        """
        return pygame.Surface correspond of LAKE type but random
        """
        return random.choice([self.tiles[7 + (i * 9)] for i in range(1,6)])


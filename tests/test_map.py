import pygame
import sys
sys.path.append(sys.path[0].replace("\\tests",""))
from src.objects.tiles import Hexagon
from src.utils import *
from src.objects.map import Mapa

def test_add_hexagon():
    mapa = Mapa()
    hexagon = Hexagon(100, 100, 50, (200, 200, 200))  # Create a hexagon object for testing
    mapa.add_hexagon(hexagon)
    assert hexagon in mapa.hexagons

def test_check_collision():
    mapa = Mapa()
    hexagon = Hexagon(100, 100, 50, (200, 200, 200))  # Create a hexagon object for testing
    mapa.add_hexagon(hexagon)
    assert mapa.check_collision(100, 100) is True  # Test collision with the hexagon
    assert mapa.check_collision(200, 200) is False  # Test no collision with the hexagon

def test_get_hexagon():
    mapa = Mapa()
    hexagon = Hexagon(100, 100, 50, (200, 200, 200))  # Create a hexagon object for testing
    mapa.add_hexagon(hexagon)
    assert mapa.get_hexagon(100, 100) == hexagon  # Test getting the hexagon at specified coordinates
    assert mapa.get_hexagon(200, 200) is None  # Test no hexagon found at specified coordinates

def test_realign_hexagons():
    mapa = Mapa()
    hexagon1 = Hexagon(100, 100, 50, (200, 200, 200))
    hexagon2 = Hexagon(200, 200, 50, (200, 200, 200))
    mapa.add_hexagon(hexagon1)
    mapa.add_hexagon(hexagon2)

    new_center = Hexagon(300, 300, 50, (200, 200, 200))  # Create a new center hexagon for testing
    mapa.realign_hexagons(new_center)

    assert hexagon1.x == 520  # Test x-coordinate adjustment
    assert hexagon1.y == 200  # Test y-coordinate adjustment
    assert hexagon2.x == 620  # Test x-coordinate adjustment
    assert hexagon2.y == 300  # Test y-coordinate adjustment
    assert hexagon1.rect == pygame.Rect(520 - RADIUS, 200 - RADIUS, 2 * RADIUS, 2 * RADIUS)  # Test rect calculation
    assert hexagon2.rect == pygame.Rect(620 - RADIUS, 300 - RADIUS, 2 * RADIUS, 2 * RADIUS)  # Test rect calculation
    # Add more assertions as needed for other properties and calculations

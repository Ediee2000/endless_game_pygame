
import math

#CONST

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800


RADIUS = 30
SIDE_LENGHT = RADIUS * math.sqrt(3)
DISTANCE = 1


PANEL_WIDTH = SCREEN_WIDTH // 5  # Largura do painel (20% da tela)
PANEL_HEIGHT = SCREEN_HEIGHT
PANEL_X = 0
PANEL_Y = 0
PANEL_COLOR = (50, 50, 50)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 100, 0)
LIGHT_BLUE = (173, 216, 230)
LIGHT_GRAY = (200, 200, 200)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BROWN = (139, 69, 19)


def get_tempo(turno):

    if turno % 12 < 6:
        return "Dia"
    return "Noite"
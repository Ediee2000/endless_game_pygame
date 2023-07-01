import pygame
from tiles import Hexagon
from ..utils import *



def draw_tile_panel(hexagon:Hexagon, screen:pygame.Surface, current_center:Hexagon, turno):
    """
    Function responsable to draw a panel for tile information
    hexagon: Hexagon
    screen: pygame Surface
    current_center: Hexagon
    turno: int
    """
    pygame.draw.rect(screen, PANEL_COLOR, pygame.Rect(PANEL_X, PANEL_Y, PANEL_WIDTH, PANEL_HEIGHT))

    # Verificar se há um hexágono selecionado
    if current_center:
        # Configurações do texto
        font = pygame.font.Font(None, 24)
        text_color = WHITE

        # Obter a categoria do hexágono
        category = current_center.category

        # Renderizar o texto da categoria
        text_surface = font.render(f"Category: {hexagon.category}", True, text_color)
        tempo_text = font.render(f"Tempo: {get_tempo(turno)}", True, text_color, turno)

        # Posicionar o texto no painel
        text_rect = text_surface.get_rect()
        text_rect.centerx = PANEL_X + PANEL_WIDTH // 2
        text_rect.centery = PANEL_Y + PANEL_HEIGHT // 20

        # Desenhar o texto no painel
        screen.blit(text_surface, text_rect)

        text_rect = text_surface.get_rect()
        text_rect.centerx = PANEL_X + PANEL_WIDTH // 2
        text_rect.centery = PANEL_Y + PANEL_HEIGHT // 20 * 2
        screen.blit(tempo_text, text_rect)

import pygame
from src.objects.map import Mapa
from src.objects.tiles import Hexagon
from src.objects.player import Player
from src.objects.panel import draw_tile_panel
from ..utils import *



class SceneGame:

    def __init__(self, screen):
        """
        Class to hold and initialize all objects and logic we use on this scene of game
        screen: pygame.Surface
        """

        self.screen = screen
        self.turno = 0

        # Criar instância do mapa
        self.mapa = Mapa()

        # Criar instância do hexágono central
        self.current_center = Hexagon((SCREEN_WIDTH + PANEL_WIDTH) // 2, 
                                SCREEN_HEIGHT // 2,
                                RADIUS,
                                WHITE,
                                category="home")
        adjacent_hexagons = []
        for direction in range(6):
            adjacent_hexagon = self.current_center.create_adjacent_hexagon(direction, self.mapa)
            if adjacent_hexagon:
                adjacent_hexagons.append(adjacent_hexagon)
                self.mapa.add_hexagon(adjacent_hexagon)
        self.mapa.add_hexagon(self.current_center)
        self.select_hexagon = self.current_center
        self.player = Player("Test", "Warrior")

    def event(self, event):
        """
        method responsable to administrate all logic events on this scene
        event: pygame.Event
        """
        if event.type == pygame.MOUSEBUTTONDOWN and event.button in [1,3]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.select_hexagon = self.mapa.get_hexagon(mouse_x, mouse_y) if self.mapa.get_hexagon(mouse_x, mouse_y) else self.select_hexagon
            if self.select_hexagon:
                if self.current_center.isin_adjacent(self.select_hexagon) and event.button == 3:
                    self.select_hexagon.discover(self.mapa)
                    print(self.select_hexagon)
                    if self.select_hexagon.category != "Lake":
                        self.mapa.realign_hexagons(self.select_hexagon)
                        self.current_center = self.select_hexagon
                    self.turno +=1
                    draw_tile_panel(self.select_hexagon, self.screen, self.current_center, self.turno)
                else:
                    print(f"Tile muito longe para ação")

    def draw(self):
        """
        method to draw all objects on this scene
        """
            
        for hex in self.mapa.hexagons:
            hex.draw(self.screen)

        self.player.draw(self.current_center.x, self.current_center.y, self.screen)
        draw_tile_panel(self.select_hexagon, self.screen, self.current_center, self.turno)
    
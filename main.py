import pygame
import math
import random
from src.utils import *
from src.objects.source_images import SourceImages
from src.scenes.game import SceneGame


# Inicialização do Pygame
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jogo com Hexagon Tiles")

src_img = SourceImages()
scene_map = SceneGame(screen)
# Loop principal do jogo
running = True


while running:
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        
        scene_map.event(event)

    
    # Preencher a tela com a cor preta
    screen.fill(BLACK)

    # Criar os hexágonos adjacentes
    scene_map.draw()


    # Atualizar a tela
    pygame.display.flip()

# Encerrar o Pygame
pygame.quit()

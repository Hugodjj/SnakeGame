import pygame
from pygame.locals import *

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

# Lógica para a criação da janela do jogo.

pygame.init()
game_screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake')

# Criação da cobrinha

snake = [(300, WINDOW_HEIGHT/2), (310, WINDOW_HEIGHT/2), (320, WINDOW_HEIGHT/2)]
skin_snake = pygame.Surface((10, 10))
skin_snake.fill((255, 255, 255)) # Branco RGB

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    game_screen.fill((0, 128, 0)) # Cor do campo Verde RGB
    for pos in snake:
        game_screen.blit(skin_snake, pos)
    pygame.display.update()

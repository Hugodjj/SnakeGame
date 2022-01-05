import pygame
from pygame.locals import *

# Lógica para a criação da janela do jogo.

pygame.init()
game_screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    pygame.display.update()

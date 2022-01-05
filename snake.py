import time

import pygame
from pygame.locals import *

# Constantes que definem o tamanho da janela. Facilita caso haja alterações no futuro

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

# Constantes para movimentação

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# Lógica para a criação da janela do jogo.

pygame.init()
game_screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake')

# Criação da cobrinha

snake = [(200, WINDOW_HEIGHT/2), (210, WINDOW_HEIGHT/2), (220, WINDOW_HEIGHT/2)]
skin_snake = pygame.Surface((10, 10))
skin_snake.fill((255, 255, 255)) # Branco RGB

snake_direction = LEFT

# Clock para diminuir a rapidez da cobrinha

clock = pygame.time.Clock()

# Função que realmente movimenta a cobrinha

"""def moviment(key_pressed):
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0],snake[i-1][1])

        if key_pressed == UP:
            snake[0] = (snake[0][0], snake[0][1] - 10)
        if key_pressed == DOWN:
            snake[0] = (snake[0][0], snake[0][1] + 10)
        if key_pressed == RIGHT:
            snake[0] = (snake[0][0] + 10, snake[0][1])
        if key_pressed == LEFT:
            snake[0] = (snake[0][0] - 10, snake[0][1])
"""
while True:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

        # Movimentação da cobra TODO Elaborar uma função para essa movimentação

    if event.type == KEYDOWN:
        if event.type == K_UP:
                snake_direction == UP
        if event.type == K_DOWN:
                snake_direction == DOWN
        if event.type == K_LEFT:
                snake_direction == LEFT
        if event.type == K_RIGHT:
                snake_direction == RIGHT

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

        if snake_direction == UP:
            snake[0] = (snake[0][0], snake[0][1] - 10)
        if snake_direction == DOWN:
            snake[0] = (snake[0][0], snake[0][1] + 10)
        if snake_direction == RIGHT:
            snake[0] = (snake[0][0] + 10, snake[0][1])
        if snake_direction == LEFT:
            snake[0] = (snake[0][0] - 10, snake[0][1])

    game_screen.fill((155, 204, 153)) # Cor do campo Verde RGB

    for pos in snake:
        game_screen.blit(skin_snake, pos)
    pygame.display.update()

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

snake = [(300, WINDOW_HEIGHT/2), (300, WINDOW_HEIGHT/2), (300, WINDOW_HEIGHT/2)]
skin_snake = pygame.Surface((15, 15))
skin_snake.fill((255, 255, 255)) # Branco RGB

snake_direction = LEFT

# Clock para diminuir a rapidez da cobrinha

clock = pygame.time.Clock()

# Função que realmente movimenta a cobrinha

def moviment(key_pressed):
    for i in range(-1,len(snake)-1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

        if key_pressed == UP:
            snake[0] = (snake[0][0], snake[0][1] - 10)
        if key_pressed == DOWN:
            snake[0] = (snake[0][0], snake[0][1] + 10)
        if key_pressed == RIGHT:
            snake[0] = (snake[0][0] + 10, snake[0][1])
        if key_pressed == LEFT:
            snake[0] = (snake[0][0] - 10, snake[0][1])

while True:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

# Lógica para detecção de ação

        if event.type == KEYDOWN:
            if event.key == K_UP and snake_direction != DOWN:
                snake_direction = UP
            elif event.key == K_DOWN and snake_direction != UP:
                snake_direction = DOWN
            elif event.key == K_LEFT and snake_direction != RIGHT:
                snake_direction = LEFT
            elif event.key == K_RIGHT and snake_direction != LEFT:
                snake_direction = RIGHT

    moviment(snake_direction)

    game_screen.fill((155, 204, 153)) # Cor do campo Verde RGB
    for pos in snake:
        game_screen.blit(skin_snake, pos)
    pygame.display.update()

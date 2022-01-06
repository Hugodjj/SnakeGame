import pygame
from pygame.locals import *
import random

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

snake = [(300, WINDOW_HEIGHT / 2), (300, WINDOW_HEIGHT / 2), (300, WINDOW_HEIGHT / 2)]
skin_snake = pygame.Surface((10, 10))
skin_snake.fill((255, 255, 255))  # Branco RGB

snake_direction = LEFT

# Clock para diminuir a rapidez da cobrinha

clock = pygame.time.Clock()


# Função que realmente movimenta a cobrinha

def moviment(key_pressed):
        for i in range(len(snake) - 1, 0, -1):
            snake[i] = (snake[i - 1][0], snake[i - 1][1])

        if key_pressed == UP:
            snake[0] = (snake[0][0], snake[0][1] - 10)
        if key_pressed == DOWN:
            snake[0] = (snake[0][0], snake[0][1] + 10)
        if key_pressed == RIGHT:
            snake[0] = (snake[0][0] + 10, snake[0][1])
        if key_pressed == LEFT:
            snake[0] = (snake[0][0] - 10, snake[0][1])


# Função para auxiliar na criação de uma maça em posição aleatória

def create_random_apple():
    x = random.randint(0,59)
    y = random.randint(0,59)
    return (x * 10, y * 10)


# Função para auxiliar a detecção de colisão entre dois objetos

def collision(obj1, obj2):
    return (obj1[0] == obj2[0]) and (obj1[1] == obj2[1])

font = pygame.font.Font('freesansbold.ttf', 18)
score = 0

apple_position = create_random_apple()
apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))

# Função que checa se a cobra atingiu a borda

def hit_edge(snake):
    if snake[0][0] == WINDOW_HEIGHT or snake[0][0] == WINDOW_WIDTH or snake[0][0] < 0 or snake[0][1] < 0:
        pygame.quit()
        exit()

# Função que checa se a cobra atingiu o próprio corpo


def hit_self(snake):
    for i in range(2, len(snake)-2):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            pygame.quit()
            exit()

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

    if collision(snake[0], apple_position):
        snake.append((0,0))
        apple_position = create_random_apple()
        score += 1

    hit_edge(snake)
    hit_self(snake)
    moviment(snake_direction)

    game_screen.fill((155, 204, 153))  # Cor do campo Verde RGB
    game_screen.blit(apple, apple_position) # Colocando a maça visivel na tela


    # Posicionando pontuação na tela e atualizando toda vez que comer uma maça

    score_font = font.render('Score: %s' % (score), True, (255, 255, 255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (500, 10)
    game_screen.blit(score_font, score_rect)

    for pos in snake:
        game_screen.blit(skin_snake, pos)
    pygame.display.update()

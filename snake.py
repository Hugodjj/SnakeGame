import pygame
from pygame.locals import *
import random
import time
import os

# Constantes que definem o tamanho da janela.

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

# Constantes para movimentação

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# Constante para melhorar leitura do jogo

game_over = False

# Constantes cores RGB

white = (255, 255, 255)
green = (155, 204, 153)
red = (255, 0, 0)
black = pygame.Color(0, 0, 0)

# Pontuação

score = 0

# Acessando pastas

principal_dir = os.path.dirname(__file__)
img_dir = os.path.join(principal_dir, 'images')
sounds_dir = os.path.join(principal_dir, 'sounds')
fonts_dir = os.path.join(principal_dir, 'fonts')

# Lógica para a criação da janela do jogo.

pygame.init()
game_screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
bg_img = pygame.image.load(os.path.join(img_dir, 'bg.jpg')).convert_alpha()
bg_img = pygame.transform.scale(bg_img, (WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake')


# Métodos que adicionam efeitos sonoros no jogo

def music_sound():
    pygame.mixer.music.load(os.path.join(sounds_dir,'BoxCat Games - CPU Talk.mp3'))
    pygame.mixer.music.play(-1)


def colision_sound():
    sound_colision = pygame.mixer.Sound(os.path.join(sounds_dir,'smw_coin.wav'))
    sound_colision.play()


# Criação da cobrinha

snake = [(300, 300), (310, 300), (320, 300)]
skin_snake = pygame.Surface((10, 10))
skin_snake.fill(white)

# Direção inicial da cobrinha

snake_direction = LEFT

# Controle de FPS

fps_controll = pygame.time.Clock()

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
    x = random.randint(0, 59)
    y = random.randint(0, 59)
    return x * 10, y * 10

# Função para auxiliar a detecção de colisão entre dois objetos

def collision(obj1, obj2):
    return (obj1[0] == obj2[0]) and (obj1[1] == obj2[1])

apple_position = create_random_apple()
apple = pygame.Surface((10, 10))
apple.fill(red)

# Função da tela de game over

def game_over_window():
    font = pygame.font.Font((os.path.join(fonts_dir,'game_over.ttf')), 200)
    game_over_surface = font.render('GAME OVER', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.center = (WINDOW_WIDTH / 2, WINDOW_WIDTH / 2)
    game_screen.fill(black)
    game_screen.blit(game_over_surface, game_over_rect)
    show_score(0)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    exit()

# Função que checa se a cobra atingiu a borda

def hit_edge(snake):
    if snake[0][0] == WINDOW_HEIGHT or snake[0][1] == WINDOW_WIDTH or snake[0][0] < 0 or snake[0][1] < 0:
        game_over_window()


# Função que checa se a cobra atingiu o próprio corpo

def hit_self(snake):
    for i in range(1, len(snake) - 1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            game_over_window()

# Mostra a pontuação na tela

def show_score(position):
    font = pygame.font.Font((os.path.join(fonts_dir,'game_over.ttf')), 75)
    score_font = font.render('Score: %s' % score, True, white)
    score_rect = score_font.get_rect()

    if position == 1:
        score_rect.topright = (590, 10)
    else:
        score_rect.midbottom = (WINDOW_HEIGHT / 2, WINDOW_WIDTH / 1.5)
        score_font = font.render('Score: %s' % score, True, red)
    game_screen.blit(score_font, score_rect)

def show_snake_in_screen():
    for pos in snake:
        game_screen.blit(skin_snake, pos)

def principal_window():
    font = pygame.font.SysFont('times new roman', 60)
    principal_window_surface = font.render('SNAKE GAME', True, white)
    principal_window_rect = principal_window_surface.get_rect()
    principal_window_rect.center = (WINDOW_WIDTH / 2, WINDOW_WIDTH / 2)
    game_screen.fill(green)
    game_screen.blit(principal_window_surface, principal_window_rect)
    pygame.display.flip()

music_sound()
while True:

    fps_controll.tick(10)
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
        snake.append((0, 0))
        apple_position = create_random_apple()
        score += 1
        colision_sound()

    hit_edge(snake)
    hit_self(snake)
    moviment(snake_direction)

    game_screen.blit(bg_img, (0, 0))
    game_screen.blit(apple, apple_position)  # Colocando a maça visivel na tela

    show_score(1)
    show_snake_in_screen()
    pygame.display.update()
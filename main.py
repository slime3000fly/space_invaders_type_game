# sapce invaiders game with pygame
# By: angater1 and slime3000fly

import sys
import pygame
from pygame import mixer
from Bullet import Bullet

pygame.init()
pygame.display.init()
fps_controller = pygame.time.Clock()

screen = pygame.display.set_mode((1080, 720))

score = 0

# reading highest score from txt
f = open('highest_score.txt', 'r')
highest_score = int(f.read())
f.close()

x_player = 1080 / 2
y_player = 720

velocity = 3
bullet_velocity = 5

fps = 120

enemy_state = 'RENDER'

wall_left = pygame.Rect(0, 0, 5, 740)
wall_right = pygame.Rect(1075, 0, 10, 740)

bullets = [Bullet(screen, 700, 'UP', 10, 10, bullet_velocity), Bullet(screen, 700, 'UP', 10, 10, bullet_velocity)]
bullets_state = ['NORENDER', 'NORENDER']
ticks_to_ignore = 0  # variable to store number of ticks to ignore key reding

# sound
mixer.music.set_volume(0.1)
mixer.music.load('Simplicity(by damn so deep).mp3')
mixer.music.play(-1)
bang_sound = mixer.Sound('bang.wav')
score_sound = mixer.Sound('score.wav')
ai_score_sound = mixer.Sound('ai_score.wav')

# color
red = pygame.Color(139, 0, 0)
blue = pygame.Color(51, 255, 255)
white = pygame.Color(255, 255, 255)
orange = (255, 100, 0)
yellow = (255, 50, 170)
green = (34, 177, 76)
black = (0, 0, 0)


# function declaration
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('  Player: ' + str(score) + '  Highest Score : ' + str(highest_score), True,
                                      color)


def lose():
    # function which play after lose game
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.QUIT: sys.exit()
        # drawing writing 'you lose'
        font = pygame.font.Font('freesansbold.ttf', 52)
        text = font.render('YOU LOSE', True, red, black)
        # text surface object
        textRect = text.get_rect()
        # set the center of the rectangular object.
        textRect.center = (540, 360)
        screen.blit(text, textRect)
        pygame.display.update()


def won():
    # function which play after lose game
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.QUIT: sys.exit()
        # drawing writing 'you lose'
        font = pygame.font.Font('freesansbold.ttf', 52)
        text = font.render('YOU WON', True, green, black)
        # text surface object
        textRect = text.get_rect()
        # set the center of the rectangular object.
        textRect.center = (540, 360)
        screen.blit(text, textRect)
        pygame.display.update()


done = False

while not done:
    # key to control
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        if x_player > 0 + 15:
            x_player -= velocity
    if pressed[pygame.K_RIGHT]:
        if x_player < 1080 - 15:
            x_player += velocity
    if pressed[pygame.K_ESCAPE]:
        done = True
    if pressed[pygame.K_SPACE]:
        for i in range(0, 2):
            if (bullets_state[i] == 'NORENDER' and ticks_to_ignore == 0):
                bullets_state[i] = 'RENDER'
                ticks_to_ignore = 10
                x_bullet = x_player - 5
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # drawing elements
    pygame.draw.rect(screen, red, wall_right)
    pygame.draw.rect(screen, red, wall_left)
    enemy_rect = pygame.Rect(1080 / 2, 720 / 2, 10, 20)
    player_rect = pygame.Rect(x_player, y_player, 20, 30)
    player_rect.center = (x_player, 700)
    pygame.draw.rect(screen, white, player_rect)
    if enemy_state == 'RENDER':
        pygame.draw.rect(screen, white, enemy_rect)

    # drawing bullet and check colision
    for i in range(0, 2):
        if (bullets_state[i] == 'RENDER'):
            if pygame.Rect.colliderect(bullets[i].draw(x_bullet, 700, bullets_state[i], i),
                                       enemy_rect):
                enemy_state = 'NOT_RENDER'
        if (bullets[i].returnY() <= -1): bullets_state[i] = 'NORENDER'

    # drawing score
    show_score(1, white, 'times new roman', 20)
    pygame.display.flip()
    screen.fill(black)

    if (ticks_to_ignore > 0): ticks_to_ignore -= 1

    # saving highest score to highest_score.txt
    f = open('highest_score.txt', 'w')
    f.write(str(highest_score))
    f.close()

    # FPS !!!!!
    fps_controller.tick(fps)

# class for enemy
# method draw enemies and make it move up

import pygame
from Bullet import Bullet


class Enemy:
    y = -10
    x = 1080 / 2
    b=0
    enemy_direction = 'RIGHT'
    bullet_status = 'NORENDER'

    def __init__(self, screen, y_enemy, x_enemy, width=20, lenght=20, enemy_velocity=5):
        self.screen = screen
        self.y = y_enemy
        self.x = x_enemy
        self.width = width
        self.lenght = lenght
        self.enemy_velocity = enemy_velocity
        self.bullet = Bullet(self.screen, self.y, 'DOWN', 10, 10, 2)

    def draw(self, max_x, min_x, object ,render='RENDER'):
        # function to draw, it return enemy which is pygame.rect to colision check
        enemy_direction = 'RIGHT'
        if (render == 'RENDER'):
            if self.x >= max_x:
                self.enemy_direction = 'LEFT'
                self.bullet_status = 'RENDER'
            if self.x <= min_x: self.enemy_direction = 'RIGHT'
            green = (0, 255, 0)
            self.enemy = pygame.Rect(self.x, self.y, self.width, self.lenght)
            pygame.draw.rect(self.screen, green, self.enemy)
            if (self.enemy_direction == 'RIGHT'): self.x += 2
            if (self.enemy_direction == 'LEFT'): self.x -= 2
            if (self.bullet_status=='RENDER'):
                self.b = pygame.Rect.colliderect(self.bullet.draw(self.x, self.y, self.bullet_status),object)
        return self.enemy


    def check_colison(self):
        print ('hit')
        return self.b

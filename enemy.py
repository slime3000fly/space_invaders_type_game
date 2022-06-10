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
    #color
    green = (0, 255, 0)

    def __init__(self, screen, y_enemy, x_enemy,max_x, min_x, width=20, lenght=20, enemy_velocity=1):
        self.screen = screen
        self.y = y_enemy
        self.x = x_enemy
        self.width = width
        self.lenght = lenght
        self.enemy_velocity = enemy_velocity
        self.bullet = Bullet(self.screen, self.y, 'DOWN', 10, 10, 2)
        self.max_x = max_x
        self.min_x = min_x

    def draw(self,object ,render='RENDER'):
        # function to draw, it return enemy which is pygame.rect to colision check
        enemy_direction = 'RIGHT'
        #establish direction for enemy and bullet status
        if (render == 'RENDER'):
            if self.x >= self.max_x:
                self.enemy_direction = 'LEFT'
                self.bullet_status = 'RENDER'
            if self.x <= self.min_x: self.enemy_direction = 'RIGHT'

            #drawing enemy
            self.enemy = pygame.Rect(self.x, self.y, self.width, self.lenght)
            pygame.draw.rect(self.screen, self.green, self.enemy)

            #calucalte x for enemy
            if (self.enemy_direction == 'RIGHT'): self.x += self.enemy_velocity
            if (self.enemy_direction == 'LEFT'): self.x -= self.enemy_velocity
            if (self.bullet_status=='RENDER'):
                #drawing bullet and check if it collide to the object
                self.b = pygame.Rect.colliderect(self.bullet.draw(self.x, self.y, self.bullet_status),object)
        return self.enemy


    def check_colison(self):
        return self.b

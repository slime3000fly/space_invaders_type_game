# class for bullet

import pygame


class Bullet:
    y = -10

    def __init__(self, screen, bullet_direction='UP', width=10, lenght=10, bullet_velocity=15):
        self.screen = screen
        self.bullet_direction = bullet_direction
        self.width = width
        self.lenght = lenght
        self.bullet_velocity = bullet_velocity

    def draw(self, x_bullet=0, y_bullet=0, render='NOREDNER', color=1):

        if self.y < 0:
            # print('przed', self.y)
            # render = 'NORENDER'
            self.y = y_bullet
            # print('po: ', self.y)
        if (render == 'RENDER'):
            # if (render == 'RENDER'):
            #     self.y = 0
            #     render = 'NORENDER'
            # if (self.y == 0):
            #     self.y = y_bullet

            red = pygame.Color(139, 0, 0)
            orange = (255, 100, 0)
            if (color == 1): c = red
            if (color == 0): c = orange
            bullet = pygame.Rect(x_bullet, self.y, self.width, self.lenght)
            pygame.draw.rect(self.screen, c, bullet)
            # print('y', self.y)
            if self.bullet_direction == 'UP':
                self.y -= self.bullet_velocity
            if self.bullet_direction == 'DOWN':
                self.y += self.bullet_velocity
    def test(self, i=20):
        red = pygame.Color(139, 0, 0)
        orange = (255, 100, 0)
        b = pygame.Rect(300, 200, 100, 100)
        c = pygame.Rect(30, 0, 100, 100)
        if i == 0:  pygame.draw.rect(self.screen, red, b)
        if i == 1:  pygame.draw.rect(self.screen, orange, c)
    def returnY(self):
        return self.y
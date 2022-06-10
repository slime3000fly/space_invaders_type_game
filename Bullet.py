# class for bullet
# method draw bullet and make it move up

import pygame


class Bullet:
    y = -10
    x = 1080 / 2

    def __init__(self, screen, y_bullet, bullet_direction='UP', width=10, lenght=10, bullet_velocity=15):
        self.screen = screen
        self.bullet_direction = bullet_direction
        self.width = width
        self.lenght = lenght
        self.bullet_velocity = bullet_velocity
        self.y = y_bullet

    def draw(self, x_bullet=0, y_bullet=0, render='NOREDNER' ):
    #function to draw, it return bullet which is pygame.rect to colision check
        if (render == 'RENDER'):
            if self.y == y_bullet:
                self.x = x_bullet
            if self.y <= -1 or self.y >= 720:
                self.y = y_bullet
                self.x = x_bullet
                # print('y', self.y)
            red = pygame.Color(139, 0, 0)
            orange = (255, 100, 0)
            c = orange
            # if (color == 1): c = red
            # if (color == 0): c = orange
            self.bullet = pygame.Rect(self.x, self.y, self.width, self.lenght)
            pygame.draw.rect(self.screen, c, self.bullet)
            if self.bullet_direction == 'UP':
                self.y -= self.bullet_velocity
            if self.bullet_direction == 'DOWN':
                self.y += self.bullet_velocity
        return self.bullet

    def returnY(self):
        return self.y

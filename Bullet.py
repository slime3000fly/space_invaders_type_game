#class for bullet

import pygame

class bullet:

    y=0
    def __init__(self,screen,x_bullet,y_bullet,bullet_direction='UP',width=10,lenght=10,bullet_velocity=15):
        self.screen = screen
        self.x_bullet = x_bullet
        self.y_bullet = y_bullet
        self.bullet_direction = bullet_direction
        self.width = width
        self.lenght = lenght
        self.bullet_velocity = bullet_velocity

    def draw(self):
        if(self.y == 0):
            self.y=self.y_bullet
        if self.y <= 0: return 0
        red = pygame.Color(139, 0, 0)
        bullet = pygame.Rect(self.x_bullet, self.y, self.width, self.lenght)
        pygame.draw.rect(self.screen, red, bullet)

        if self.bullet_direction == 'UP':
            self.y -= self.bullet_velocity
        if self.bullet_direction == 'DOWN':
            self.y += self.bullet_velocity

        return self.y



import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, exercise):
        super().__init__()
        self.screen = exercise.screen
        self.settings = exercise.settings
        self.color = self.settings.bullet_color
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midright = exercise.ship.rect.midright
        self.x = float(self.rect.x)

    def update(self):
        """перемещает снаряд вправо по экрану"""
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
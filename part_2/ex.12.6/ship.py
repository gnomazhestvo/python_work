import pygame

class Ship:
    def __init__(self, exercise):
        self.screen = exercise.screen
        self.settings = exercise.settings
        self.screen_rect = exercise.screen.get_rect()
        self.image = pygame.image.load('ship.png')
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        self.moving_up = False
        self.moving_down = False
        self.y = float(self.rect.y)

    def movings(self):
        if self.moving_up and self.rect.top >= 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Класс управления пришельцами."""

    def __init__(self, exercise):
        """Инициализирует пришельца и задает начальную позицию."""
        super().__init__()
        self.screen = exercise.screen
        self.screen_rect = exercise.screen.get_rect()
        self.settings = exercise.settings

        # загрузка изображения пришельца и назначение атрибута rect:
        self.image = pygame.image.load('alien.bmp')
        self.rect = self.image.get_rect()

        # каждый новый пришелец появляется в левом верхнем углу экрана,
        # удаленном от левого края на ширину пришельца, и удаленном от
        # верха экрана на высоту пришельца:
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # сохранение точной позиции пришельца:
        self.x = self.rect.x
        self.y = self.rect.y

    def update(self):
        """Отвечает за движение пришельцев."""
        self.y += self.settings.alien_speed * self.settings.alien_direction
        self.rect.y = self.y

    def check_edges(self):
        """Возвращает True, если пришелец находится у края экрана."""
        return (self.rect.top <= 0) or (self.rect.bottom >= self.screen_rect.bottom)
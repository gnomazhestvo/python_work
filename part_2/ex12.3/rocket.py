# 12.4. Ракета. Создайте игру, у которой в исходном состоянии в центре экрана
# находится ракета. Игрок может перемещать ракету вверх, вниз, вправо и влево
# четырьмя клавишами со стрелками. Проследите за тем, чтобы ракета не выходила
# за края экрана.

import sys
import pygame

class Exercise:
    """Класс упражнения с ракетой."""

    def __init__ (self):
        """Инициализирует параметры."""
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.rocket = Rocket(self)
        pygame.display.set_caption('Exercise 12.3')
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.bg_color = (230, 230, 230)

    def _check_events(self, event):
        """Отслеживает действия."""
        if event.type == pygame.KEYDOWN:
            self._check_keydown_events(event)
        elif event.type == pygame.KEYUP:
            self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Отслеживает нажатие кнопок."""
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
    
    def _check_keyup_events(self, event):
        """Отслеживает отпускание кнопок"""
        if event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False   

    def run_rocket(self):
        """Основной цикл упражнения, запускает ракету."""
        while True:
            self.clock.tick(self.fps)
            self.screen.fill(self.bg_color)
            self.rocket.blitme()
            pygame.display.flip()
            self.rocket.movings()
            for event in pygame.event.get():
                self._check_events(event)     


class Rocket:
    """Класс ракеты."""

    def __init__(self, rocket_exercise):
        self.screen = rocket_exercise.screen
        self.screen_rect = rocket_exercise.screen.get_rect()
        self.image = pygame.image.load('rocket.png')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        self.speed = 10
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def movings(self):
        """Отвечает за передвижение ракеты в границах экрана."""
        if self.moving_up and self.rect.y>0:
            self.rect.y -= self.speed
        if self.moving_down and self.rect.bottom<self.screen_rect.bottom:
            self.rect.y += self.speed
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.rect.x += self.speed
        if self.moving_left and self.rect.x>0:
            self.rect.x -= self.speed

    def blitme(self):
        """Отрисовывает ракету на экране."""
        self.screen.blit(self.image, self.rect)

rr = Exercise()
rr.run_rocket()
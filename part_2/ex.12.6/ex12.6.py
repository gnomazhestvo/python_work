import sys
import pygame

from random import randint

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class Exercise:
    def __init__(self):
        pygame.init()
        # инициализация параметров:
        self.settings = Settings(self)
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Ex. 12.6.')
        # fps:
        self.clock = pygame.time.Clock()
        # инициализация модулей - корабль, снаряд, пришельцы:
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        # создает пришельца:
        self._create_fleet()

    def _update_screen(self):
        """Заливает экран, выводит корабль, снаряды и пришельцев."""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        pygame.display.flip()


    def _check_events(self):
        for event in pygame.event.get():
            self._check_keydown_events(event)
            self._check_keyup_events(event)
            
    def _check_keydown_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.ship.moving_up = True
            if event.key == pygame.K_DOWN:
                self.ship.moving_down = True
            if event.key == pygame.K_SPACE:
                self._fire_bullets()
            if event.key == pygame.K_q:
                sys.exit()

    def _check_keyup_events(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.ship.moving_up = False
            elif event.key == pygame.K_DOWN:
                self.ship.moving_down = False


    def _fire_bullets(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().right:
                self.bullets.remove(bullet)


    def _create_alien(self, x_pos, y_pos):
        """Создает пришельца в точке с координатами x, y."""
        new_alien = Alien(self)
        new_alien.x = x_pos
        new_alien.y = y_pos
        new_alien.rect.x = new_alien.x
        new_alien.rect.y = new_alien.y
        self.aliens.add(new_alien)

    def _create_fleet(self):
        """Вычисляет вместительность экрана и заполняет его пришельцами."""
        sample_alien = Alien(self)
        alien_width, alien_height = sample_alien.rect.size
        screen_width, screen_height = self.screen.get_size()
        current_y = alien_height
        while current_y <= (screen_height - 2 * alien_height):
            current_x = 10 * alien_width
            while current_x <= (screen_width - alien_width):
                self._create_alien(current_x, current_y)
                current_x += alien_width * 2
            current_x = screen_width
            current_y += alien_height * 2
        current_y = screen_height

    def _change_fleet_direction(self):
        """Отвечает за скорость пришельцев по y, и меняет направление их движения
        по x, когда они достигают края экрана,"""
        for alien in self.aliens.sprites():
            alien.rect.x -= self.settings.alien_y_speed
        self.settings.alien_direction *= -1

    def _check_fleet_edges(self):
        """Проверяет достижение пришельцем края экрана."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()


    def run_exercise(self):
        while True:
            self._check_events()
            self.ship.movings()
            self._update_aliens()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)


rr = Exercise()
if __name__ == '__main__':
    rr.run_exercise()
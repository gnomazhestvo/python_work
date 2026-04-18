import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class Exercise:
    def __init__(self):
        pygame.init()
        self.settings = Settings(self)
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Ex. 12.6.')
        self.clock = pygame.time.Clock()
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
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

    def run_exercise(self):
        while True:
            self._check_events()
            self.ship.movings()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)


rr = Exercise()
if __name__ == '__main__':
    rr.run_exercise()
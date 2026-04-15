import sys
import pygame

class BlueScreen:
    """Инициализирует процесс создания человечка на синем фоне."""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.goblin = Goblin(self)
        
        pygame.display.set_caption('Blue Yeti')

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit
            pygame.display.flip()
            self.screen.fill((0, 191, 255))
            self.goblin.blitme()


class Goblin:
    """Класс гоблин."""

    def __init__(self, blueyeti):
        self.screen = blueyeti.screen
        self.screen_rect = blueyeti.screen.get_rect()
        self.image = pygame.image.load('goblin-back-slash.gif')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)


if __name__ == '__main__':
    start = BlueScreen()
    start.run()
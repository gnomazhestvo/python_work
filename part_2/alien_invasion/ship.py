import pygame

class Ship:
    """Класс для управления кораблем."""

    def __init__(self, ai_game):
        """Инициализирует корабль и задает его начальную позицию."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # загружает изображение и получает прямоугольник
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        # каждый новый корабль появляется внизе в середине
        self.rect.midbottom = self.screen_rect.midbottom
        # флаги перемещения корабля:
        self.moving_right = False
        self.moving_left = False
        self.settings = ai_game.settings
        # зададим атрибут координаты прямоугольника и превратим ее в float, 
        # чтобы можно было передавать в нее дробные значения:
        self.x = float(self.rect.x)

    def update(self):
        """Отслеживает состояние флагов перемещения корабля."""
        if self.moving_right:
            if self.rect.right < self.screen_rect.right:
                self.x += self.settings.ship_speed
        if self.moving_left:
            if self.rect.left > 0:
                self.x -= self.settings.ship_speed
        # обновляем координату x после того как она была переведна во float:
        self.rect.x = self.x

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)
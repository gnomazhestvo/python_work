class Settings:
    """Класс для хранения настроек игры."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # параметры экрана
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        # параметры корабля:
        self.ship_speed = 1.5
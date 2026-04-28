class Settings:
    def __init__(self, exercise):
        # настройки экрана
        self.bg_color = (230, 230, 230)
        # настройки корабля
        self.ship_speed = 3
        # настройки снаряда
        self.bullet_color = (15, 15, 15)
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_speed = 10
        # настройки пришельца
        self.alien_speed = 1
        self.alien_direction = -1
        self.alien_y_speed = 5
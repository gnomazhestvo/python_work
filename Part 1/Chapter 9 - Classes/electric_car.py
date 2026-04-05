from car import Car

class Battery:
    """Простая модель аккумулятора электромобиля."""

    def __init__(self, battery_size=40):
        """Инициализирует атрибуты аккумулятора."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Выводит данные о приблизительном запасе хода
        для аккумулятора."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        else:
            print("Error! We don't have such batteries... Please, contact us.")
        print(f"This car can go about {range} km on a full charge.")
    
    def upgrade_battery(self):
        if self.battery_size == 65:
            print('You already have the best battery!')
        else:
            self.battery_size = 65
            print(f'Your battery has been upgraded to {self.battery_size} kWh!')




class ElectricCar(Car):
    """Представляет аспекты машины, специфические для электромобилей"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
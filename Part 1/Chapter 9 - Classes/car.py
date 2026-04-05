class Car:
    """Простая модель автомобиля"""

    def __init__(self, make, model, year):
        """Инициализирует атрибуты описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Возвращает отформатированное описание."""
        long_name = f"{self.year} {self.make} {self.model}"
        print(long_name.title())
    
    def read_odometer(self):
        """Выводит информацию о пробеге машины."""
        print(f"This car has {self.odometer_reading} km on it.")

    def update_odometer(self, mileage):
        """Устанавливает на одометре заданное значение.
        При попытке скрутки изменение отклоняется."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Увеличивает показания одометра с заданным приращением.
        При попытке скрутки изменение отклоняется."""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")
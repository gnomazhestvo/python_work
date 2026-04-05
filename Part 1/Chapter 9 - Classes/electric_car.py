class Car:
    """Простая модель автомобиля"""

    def __init__(self, make, model, year):
        """Инициализация атрибутов"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Возвращает отформатированное описание"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
    
    def read_odometer(self):
        """Выводит данные о пробеге машины"""
        print(f"This car har {self.odometer_reading} km on board.")
    
    def update_odometer(self, mileage):
        """Устанавливает на одометре заданное значение"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can not roll back the odometer!')
        
    def increment_odometer(self, miles):
        """Увеличивает показания одометра на заданное значение"""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print('You can not roll back the odometer!')
    

class ElectricCar(Car):
    """Представляет специфические аспекты электромобилей"""

    def __init__(self, make, model, year):
        """Инициализирует атрибуты класса-родителя"""
        super().__init__(make, model, year)


my_leaf = ElectricCar('Nissan', 'Leaf', 2024)
print(my_leaf.get_descriptive_name())
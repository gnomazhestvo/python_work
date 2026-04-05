print()

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
        return long_name.title()
    
    def read_odometer(self):
        """Выводит данные о пробеге машины"""
        print(f"Пробег машины - {self.odometer_reading} км.")

    def update_odometer(self, mileage):
        """Устанавливает показания одометра.
        При попытке скрутки пробега изменение отклоняется"""
        if mileage < self.odometer_reading:
            print('Не скручивайте пробег!')
        else:
            self.odometer_reading = mileage
    
    def increment_odometer(self, km):
        if km < 0:
            print('Не скручивайте пробег!')
        else:
            self.odometer_reading += km
    
my_new_car = Car('mercedes-benz', 'slk-200', '2011')

print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(999)
my_new_car.read_odometer()
print()

my_new_car.increment_odometer(-100)
my_new_car.read_odometer()
print()

my_new_car.update_odometer(999)
my_new_car.read_odometer()
print()

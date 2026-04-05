# 9.10. Импортирование класса Restaurant.
# Возьмите последнюю версию класса Restaurant и сохраните ее
# в модуле. Создайте отдельный файл, импортирующий этот класс.
# Создайте экземпляр Restaurant и вызовите один из методов
# Restaurant, чтобы показать, что оператор import работает
# правильно.
# 
# Этот файл - модуль Restaurant для упражнения 9.10.

class Rest:
    """класс ресторан..."""
    
    def __init__(self, rest_name, cuisine_type):
        """инициализирует атрибуты"""
        self.rest_name = rest_name
        self.cuisine_type = cuisine_type
    
    def describe_rest(self):
        print(f'Ресторан {self.rest_name}, кухня - {self.cuisine_type}.')

    def open_rest(self):
        print(f'{self.rest_name} открыт.')


class IceCreamStand(Rest):
    def __init__ (self, rest_name, cuisine_type, *flavors):
        super().__init__(rest_name, cuisine_type)
        self.flavors = flavors

    def get_flavors_list(self):
        """выводит список вкусов мороженного. Если список не
        задан при вызове функции, то выводится список по умолчанию"""
        print(f'Список сортов мороженного:')
        if not self.flavors:
            self.flavors = ['шоколадное', 'ореховое', 'фисташковое']
        for flavor in self.flavors:
            print(f'- {flavor}')
# 9.6. Киоск с мороженым.
# Киоск с мороженым — особая разновидность ресторана.
# Напишите класс IceCreamStand, наследуемый от класса
# Restaurant из упражнения 9.1 или 9.4. Подойдет любая версия
# класса; просто выберите ту, которая вам больше нравится.
# Добавьте атрибут flavors для хранения списка сортов
# мороженого. Напишите метод, который выводит этот список.
# Создайте экземпляр IceCreamStand и вызовите данный метод.
print('\n9.6. Киоск с мороженным.\n')


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



# описываем ресторан Nomi
rest_0 = Rest('Nomi', 'китайская')
rest_0.describe_rest()
rest_0.open_rest()
print()

# описываем киоск мороженного
my_ice_cream = IceCreamStand('Ice Cream', 'мороженное', 'ореховое', 'малиновое', 'клубничное')
my_ice_cream.describe_rest()
my_ice_cream.open_rest()
my_ice_cream.get_flavors_list()

print('\n== == == ==\n')



# 9.7. Администратор.
# Администратор — особая разновидность пользователя. Напишите
# класс Admin, наследуемый от класса User из упражнения 9.3
# или 9.5. Добавьте атрибут privileges для хранения списка
# строк вида "разрешено добавлять сообщения", "разрешено
# удалять пользователей", "разрешено банить пользователей"
# и т.д. Напишите метод show_privileges() для вывода набора
# привилегий администратора. Создайте экземпляр Admin и
# вызовите свой метод.
# 
# 9.8. Привилегии.
# Напишите класс Privileges. Класс должен содержать всего
# один атрибут privileges со списком строк из упражнения 9.7.
# Переместите метод show_privileges() в этот класс. Создайте
# экземпляр Privileges как атрибут класса Admin. Создайте
# новый экземпляр Admin и используйте свой метод для вывода
# списка привилегий.

print('9.7. Администратор.\n9.8. Привилегии.\n')



class User:
    """профиль пользователя"""
    def __init__(self, name, surname, photo='', birthday='', notification_marker='отключены'):
        """инициализация аргументов"""
        self.name = name
        self.surname = surname
        self.role = 'User'
        self.photo = photo
        self.birthday = birthday
        self.notification_marker = notification_marker
        self.login_attempts = 0

    def describe_user(self):
        """вывод полей с описанием"""
        print(f"Пользователь: {self.name.title()} {self.surname.title()}.")
        if self.photo:
            print(f"Фото: {self.photo}.")
        if self.birthday:
            print(f"Дата рождения: {self.birthday}.")
        print(f"Уведомления: {self.notification_marker}.")

    def greet_user(self):
            """приветствует пользователя"""
            print(f"{self.name.title()} {self.surname.title()}, добро пожаловать.", end =' ')
            print(f"Ваша роль в системе: {self.role}.")

    def increment_login_attempts(self):
        """Увеличивает счетчик входов на 1"""
        self.login_attempts += 1

    def show_login_attempts(self):
        print(f'Количество попыток входа пользователя {self.name.title()}: {self.surname.title()}: {self.login_attempts}')

    def reset_login_attempts(self):
        """Сбрасывает попытки входа"""
        self.login_attempts = 0
    


    
class Privileges:
    def __init__(self):
        self.privileges = ['Разрешено добавлять сообщения', 
                           'Разрешено удалять пользователей',
                           'Разрешено банить пользователей']

    def show_privileges(self):
        for privilege in self.privileges:
            print(f'- {privilege}')
            


class Admin(User):
    def __init__(self, name, surname, photo, birthday, notification_marker):
        super().__init__(name, surname, photo, birthday, notification_marker)
        self.role = 'Admin'
        self.admin = Privileges()


user_0 = User('lev', 'volkov', 'nature', notification_marker='включены')
user_1 = Admin('roman', 'smirnov', 'отсутствует', '24.09.1996', 'включены')
user_2 = Admin('настя', 'шкурина', 'красоточка', '20.09.2000', 'выключены')

users = [user_0, user_1, user_2]

# Выводим описание пользователей:
for user in users:
    user.describe_user()
    user.greet_user()
    if user.role == 'Admin':
        user.admin.show_privileges()
    print()
print('\n== == == ==\n')


# 9.9. Обновление аккумулятора.
# Используйте окончательную версию программы electric_car.py
# из этого раздела. Добавьте в класс Battery метод
# upgrade_battery(). Он должен проверять размер аккумулятора
# и устанавливать мощность равной 65, если она имеет другое
# значение. Создайте экземпляр электромобиля с аккумулятором
# по умолчанию, вызовите get_range(), а затем вызовите его
# еще раз после upgrade_battery(). Убедитесь в том, что запас
# хода увеличился.
print('9.9. Обновление аккумулятора.')


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
        print(f"This car has {self.odometer_reading} km on board.")
    
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

    def fill_gas_tank(self):
        print(120)



class Battery:
    """Простая модель аккумуляторра электромобиля"""
    def __init__(self, battery_size=40):
        """Инициализирует атрибуты аккумулятора"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора"""
        print(f"This car has a {self.battery_size}-kWh battery on board.")

    def get_range(self):
        """Выводит данные о приблизительном запасе хода"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} km on a full charge.")
    
    def upgrade_battery(self):
        if self.battery_size == 65:
            print('You already have the best battery!')
        else:
            self.battery_size = 65
            print(f'Your battery has been upgraded to {self.battery_size} kWh!')



class ElectricCar(Car):
    """Представляет специфические аспекты электромобилей"""

    def __init__(self, make, model, year):
        """Инициализирует атрибуты класса-родителя,
        затем инициализирует специфические атрибуты электромобилей"""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print('Electric car has no gas tank!')



my_leaf = ElectricCar('Nissan', 'Leaf', 2024)

print(f'\n{my_leaf.get_descriptive_name()}')
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()
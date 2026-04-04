# 9.1. Ресторан.
# Создайте класс Restaurant. Его метод __init__() должен
# содержать два атрибута: restaurant_name и cuisine_type.
# Создайте метод describe_restaurant(), который выводит два
# атрибута, и метод open_restaurant(), который выводит
# сообщение о том, что ресторан открыт.
# 
# Создайте на основе своего класса экземпляр restaurant.
# Выведите два атрибута по отдельности, затем вызовите оба
# метода.

print("9.1. Ресторан.\n")

class Rest:
    """класс ресторан..."""
    
    def __init__(self, rest_name, cuisine_type, time_from, time_to):
        """инициализирует атрибуты"""
        self.rest_name = rest_name
        self.cuisine_type = cuisine_type
        self.time_from = time_from
        self.time_to = time_to
    
    def describe_rest(self):
        print(f'Ресторан "{self.rest_name}", кухня - {self.cuisine_type}.')

    def open_rest(self):
        print(f'Ресторан открыт с {self.time_from} до {self.time_to}')

rest_0 = Rest('Nomi', 'китайская', '9:00', '18:00')

print(rest_0.rest_name)
print(rest_0.cuisine_type)
print()

rest_0.describe_rest()
rest_0.open_rest()

print('\n== == == ==\n')

# 9.2. Три ресторана.
# Создайте три разных экземпляра и вызовите для каждого 
# экземпляра метод describe_restaurant().
print("9.2. Три ресторана.\n")

class Rest2:
    """то же самое, что и в предыдущем упражнении"""
    def __init__(self, rest_name, cuisine_type):
        """инициализация аргументов"""
        self.rest_name = rest_name
        self.cuisine_type = cuisine_type

    def describe_rest(self):
        """аргумент - селф"""
        print(f'Ресторан - "{self.rest_name}", кухня - {self.cuisine_type}.')

    def open_rest(self):
        print(f'Ресторан "{self.rest_name}" открыт для посещения.')


rest1 = Rest2("Naomi Campbell", "русская")
rest2 = Rest2("Джараксус", "адская")
rest3 = Rest2("Дрыжеглот", "болотная")

rests = [rest1, rest2, rest3]
rest_names = [rest1.rest_name, rest2.rest_name, rest3.rest_name]

print(f'такс такс такс... ресторанов на выбор сегодня {len(rests)}. Это:')


for i in range(len(rest_names)):
    print(i+1, end='.) ')
    rests[i].describe_rest()
    rests[i].open_rest()
    print()

print('== == == ==\n')

# 9.3. Пользователи.
# Создайте класс User и два атрибута first_name и last_name,
# а затем еще несколько атрибутов, которые обычно хранятся в
# профиле пользователя. Напишите метод describe_user(), который
# выводит сводку с информацией о пользователе. Создайте еще
# один метод — greet_user(), позволяющий вывести персональное
# приветствие для пользователя.
# Создайте несколько экземпляров, представляющих разных
# пользователей. Вызо­вите оба метода для каждого пользователя.
print('9.3. Пользователи.\n')

class User:
    """профиль пользователя"""
    def __init__(self, name, surname, photo='', birthday='', notification_marker='отключены'):
        """инициализация аргументов"""
        self.name = name
        self.surname = surname
        self.photo = photo
        self.birthday = birthday
        self.notification_marker = notification_marker

    def describe_user(self):
        print(f"Пользователь: {self.name.title()} {self.surname.title()}.")
        if self.photo:
            print(f"Фото: {self.photo}.")
        if self.birthday:
            print(f"Дата рождения: {self.birthday}.")
        print(f"Уведомления: {self.notification_marker}")

    def greet_user(self):
            print(f"{self.name.title()} {self.surname.title()}, добро пожаловать.")

user_0 = User('lev', 'volkov', 'nature', notification_marker='включены')
user_1 = User('roman', 'smirnov', 'отсутствует', '24.09.1996', 'включены')
user_2 = User('настя', 'шкурина', 'красоточка', '20.09.2000')

users = [user_0, user_1, user_2]

for user in users:
    user.describe_user()
    user.greet_user()
    print()
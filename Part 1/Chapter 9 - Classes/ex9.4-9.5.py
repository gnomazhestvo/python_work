# 9.4. Посетители.
# Начните с программы из упражнения 9.1. Добавьте атрибут
# number_served со значением по умолчанию 0; он представляет
# количество обслуженных посетителей. Создайте экземпляр
# restaurant. Выведите значение number_served, потом измените
# и выведите снова.
# 
# Добавьте метод set_number_served(), позволяющий задать
# количество обслуженных посетителей. Вызовите его с новым
# числом, снова выведите значение.
# 
# Добавьте метод increment_number_served(), который
# увеличивает количество обслуженных посетителей на заданную
# величину. Вызовите его с любым числом, которое могло бы
# представлять количество обслуженных клиентов — скажем, за
# один день.
# 
# Программа из упражнения 9.1: 
# print("9.1. Ресторан.\n")

# class Rest:
#     """класс ресторан..."""
    
#     def __init__(self, rest_name, cuisine_type, time_from, time_to):
#         """инициализирует атрибуты"""
#         self.rest_name = rest_name
#         self.cuisine_type = cuisine_type
#         self.time_from = time_from
#         self.time_to = time_to
    
#     def describe_rest(self):
#         print(f'Ресторан "{self.rest_name}", кухня - {self.cuisine_type}.')

#     def open_rest(self):
#         print(f'Ресторан открыт с {self.time_from} до {self.time_to}')

# rest_0 = Rest('Nomi', 'китайская', '9:00', '18:00')

# print(rest_0.rest_name)
# print(rest_0.cuisine_type)
# print()

# rest_0.describe_rest()
# rest_0.open_rest()

# print('\n== == == ==\n')

print('9.4. Посетители.\n')

class Rest:
    """класс ресторан..."""
    
    def __init__(self, rest_name, cuisine_type, time_from, time_to):
        """инициализирует атрибуты"""
        self.rest_name = rest_name
        self.cuisine_type = cuisine_type
        self.time_from = time_from
        self.time_to = time_to
        self.number_served = 0 # кол-во обслуженных посетит.
    
    def describe_rest(self):
        """выводит название ресторана и кухн/"""
        print(f'Ресторан "{self.rest_name}", кухня - {self.cuisine_type}.')

    def open_rest(self):
        """выводит время работы ресторана"""
        print(f'Ресторан открыт с {self.time_from} до {self.time_to}')

    def set_number_served(self, number_served):
        """задает количество обслуженных посетителей"""
        if number_served < 0:
            print('Количество гостей не может быть отрицательным!')
        else:
            self.number_served = number_served
        print(f'В ресторане {self.rest_name} обслужено посетителей {self.number_served}.')

    def increment_number_served(self, increment):
        """увеличивает число обслуженных посетителей на
        заданную величину"""
        if increment < 0:
            print('Количество гостей не может быть отрицательным!')
        else:
            self.number_served += increment
            print(f'За день обслужено: {self.number_served}')

        

rest_0 = Rest('Nomi', 'китайская', '9:00', '18:00')

rest_0.describe_rest()
rest_0.open_rest()
print()

print(f'В ресторане {rest_0.rest_name} обслужено посетителей {rest_0.number_served}.\n')
rest_0.set_number_served(12)
print()
rest_0.increment_number_served(12)

print('\n== == == ==\n')

# 9.5. Попытки входа.
# Добавьте атрибут login_attempts в класс User из упражнения
# 9.3. Напишите метод increment_login_attempts(), увеличивающий
# значение login_attempts на 1. Напишите еще один метод,
# reset_login_attempts(), обнуляющий значение login_attempts.
# 
# Создайте экземпляр класса User и вызовите
# increment_login_attempts() несколько раз. Выведите значение
# login_attempts, чтобы убедиться в том, что значение было
# изменено правильно, а затем вызовите reset_login_attempts().
# Снова выведите login_attempts и убедитесь в том, что
# значение обнулилось. 
# 
# Программа из упражнения 9.3:
# print('9.3. Пользователи.\n')

# class User:
#     """профиль пользователя"""
#     def __init__(self, name, surname, photo='', birthday='', notification_marker='отключены'):
#         """инициализация аргументов"""
#         self.name = name
#         self.surname = surname
#         self.photo = photo
#         self.birthday = birthday
#         self.notification_marker = notification_marker

#     def describe_user(self):
#         """вывод полей с описанием"""
#         print(f"Пользователь: {self.name.title()} {self.surname.title()}.")
#         if self.photo:
#             print(f"Фото: {self.photo}.")
#         if self.birthday:
#             print(f"Дата рождения: {self.birthday}.")
#         print(f"Уведомления: {self.notification_marker}.")

#     def greet_user(self):
#             """приветствует пользователя"""
#             print(f"{self.name.title()} {self.surname.title()}, добро пожаловать.")

# user_0 = User('lev', 'volkov', 'nature', notification_marker='включены')
# user_1 = User('roman', 'smirnov', 'отсутствует', '24.09.1996', 'включены')
# user_2 = User('настя', 'шкурина', 'красоточка', '20.09.2000')

# users = [user_0, user_1, user_2]

# for user in users:
#     user.describe_user()
#     user.greet_user()
#     print()

print('9.5. Попытки входа.\n')

class User:
    """профиль пользователя"""
    def __init__(self, name, surname, photo='', birthday='', notification_marker='отключены'):
        """инициализация аргументов"""
        self.name = name
        self.surname = surname
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
            print(f"{self.name.title()} {self.surname.title()}, добро пожаловать.")

    def increment_login_attempts(self):
        """Увеличивает счетчик входов на 1"""
        self.login_attempts += 1

    def show_login_attempts(self):
        print(f'Количество попыток входа пользователя {self.name.title()}: {self.surname.title()}: {self.login_attempts}')

    def reset_login_attempts(self):
        """Сбрасывает попытки входа"""
        self.login_attempts = 0

user_0 = User('lev', 'volkov', 'nature', notification_marker='включены')
user_1 = User('roman', 'smirnov', 'отсутствует', '24.09.1996', 'включены')
user_2 = User('настя', 'шкурина', 'красоточка', '20.09.2000')

users = [user_0, user_1, user_2]

# Выводим описание пользователей:
for user in users:
    user.describe_user()
    user.greet_user()
    print()

# Актуализируем количество попыток входа:
for i in range(26):
    user_0.increment_login_attempts()
for i in range(14):
    user_1.increment_login_attempts()
for i in range (87):
    user_2.increment_login_attempts()

# Выводим количество попыток входа:
for user in users:
    user.show_login_attempts()
print()

# Обнуляем количество попыток входа и снова выводим счетчик:
for user in users:
    user.reset_login_attempts()
    user.show_login_attempts()
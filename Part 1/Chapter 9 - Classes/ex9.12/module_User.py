# 9.12. Множественные модули.
# Сохраните класс User в одном модуле, а классы Privileges
# и Admin — в другом. В отдельном файле создайте экземпляр
# Admin и вызовите метод show_privileges(), чтобы показать,
# что все работает правильно.
# 
# Этот файл - модуль User для упражнения 9.12.

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
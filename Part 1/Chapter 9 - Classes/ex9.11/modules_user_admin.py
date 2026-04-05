# 9.11. Импортирование класса Admin.
# Начните с версии класса из упражнения 9.8. Сохраните классы
# User, Privileges и Admin в одном модуле. Создайте отдельный
# файл, затем экземпляр Admin и вызовите метод
# show_privileges(), чтобы показать, что все работает
# правильно.
# 
# Этот файл - модуль для упражнения 9.11.

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
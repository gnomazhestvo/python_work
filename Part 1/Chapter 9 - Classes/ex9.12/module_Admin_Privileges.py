# 9.12. Множественные модули.
# Сохраните класс User в одном модуле, а классы Privileges
# и Admin — в другом. В отдельном файле создайте экземпляр
# Admin и вызовите метод show_privileges(), чтобы показать,
# что все работает правильно.
# 
# Этот файл - модуль с Admin и Privileges для упражнения 9.12.

from module_User import User

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
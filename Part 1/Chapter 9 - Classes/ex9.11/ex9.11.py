# 9.11. Импортирование класса Admin.
# Начните с версии класса из упражнения 9.8. Сохраните классы
# User, Privileges и Admin в одном модуле. Создайте отдельный
# файл, затем экземпляр Admin и вызовите метод
# show_privileges(), чтобы показать, что все работает
# правильно.
# 
# Этот файл - исполнительный для упражнения 9.11.

from modules_user_admin import User, Privileges, Admin

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
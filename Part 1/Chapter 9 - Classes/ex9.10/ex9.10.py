# 9.10. Импортирование класса Restaurant.
# Возьмите последнюю версию класса Restaurant и сохраните ее
# в модуле. Создайте отдельный файл, импортирующий этот класс.
# Создайте экземпляр Restaurant и вызовите один из методов
# Restaurant, чтобы показать, что оператор import работает
# правильно.
#
# Этот файл - исполнительный файл для упражнения 9.10.

# Импортируем классы.
from rest_module import Rest
from rest_module import IceCreamStand

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
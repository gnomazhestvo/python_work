from car import Car
from electric_car import ElectricCar

my_leaf = ElectricCar('Nissan', 'Leaf', 2024)
print()

my_leaf.get_descriptive_name()
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
print()

my_mercedes = Car('Mercedes-Benz', 'SLK 200', 2011)
my_mercedes.get_descriptive_name()
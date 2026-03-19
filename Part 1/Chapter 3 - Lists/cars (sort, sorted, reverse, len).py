##сортировка навсегда - .sort()
print()
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars, '\n')

cars.sort(reverse = True)
print(cars, '\n===\n')

##временная сортировка - .sorted()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print('Here is the original list:\n', cars)
print('Here is the sorted list:\n', sorted(cars, reverse = True))
print('Here is the original list again:\n', cars, '\n')
print('===\n')

##вывод списка в обратном порядке - .reverse()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print('Here is the original list:\n', cars)
cars.reverse()
print('Here is the reversed list:\n', cars)
print('\n===\n')

##определение длины списка - len()
len(cars)
print('Длина списка - ', len(cars))
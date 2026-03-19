print()
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
print()
motorcycles[0] = 'ducati'
print(motorcycles)
print()

#метод append()
motorcycles[0] = 'honda'
motorcycles.append('ducatti')
print(motorcycles)
print()

###more append()

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
print()

#метод insert
motorcycles.insert(0, 'ducati')
print(motorcycles)
print()

#оператор del
del motorcycles[0]
del motorcycles[0]
print(motorcycles)

print()
motorcycles = ['honda', 'yamaha', 'suzuki']
print('Изначальный список: ', motorcycles)
popped_motorcycle = motorcycles.pop()
print('Список после pop(): ', motorcycles)
print('Попнутый элемент списка: ', popped_motorcycle)
print()
last_owned = motorcycles.pop()
first_owned = motorcycles.pop(0)
print(f'The last motorcycle I owned was a {last_owned.title()}')
print(f'The first motorcycle I owned was {first_owned.title()}')

#remove
motorcycles = ['yamaha', 'ducati', 'honda', 'suzuki']
print(f'Полный набор мотоциклов: ', motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(f"It's better to exclude expensive ones. A {too_expensive.title()} looks too expensive. New list of motorcycles:")
print(motorcycles)
print()
print(f"Now let's try to get excluded bikes back. {too_expensive.title()} was excluded")
motorcycles.append(too_expensive)
print(motorcycles)
print()
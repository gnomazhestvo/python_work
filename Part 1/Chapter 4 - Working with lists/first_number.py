for value in range(1, 6):
    print(value)

numbers = range(1,6)
print(numbers)

numbers = list(range(1,6))
print(numbers)

##списки с заданным шагом (третий аргумент функции range):
even_numbers = list(range(2,11,2))
print(even_numbers)

multiple_5_numbers = list(range(0, 56, 5))
print(multiple_5_numbers)

square_numbers = []
print('Выводим квадраты чисел от 1 до 10.')
for number in range (1, 11):
    square_numbers.append(number**2)
    print(f'{number}^2 = {number ** 2}')
print('Блин, класс.')

## Функции работы с числовыми списками:
digits = list(range(0, 10001))
fmin = min(digits)
fmax = max(digits)
fsum = sum(digits)
print(fmin, fmax, fsum)

## Генератор списков
square_numbers = [number**2 for number in range (1, 11)]
print(square_numbers)
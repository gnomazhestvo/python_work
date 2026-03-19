### 4.3. Считаем до 20.
#вариант через цикл for с телом:
print()
digits = list(range(1, 21))
for digit in digits:
    if digit == 20:
        print(digit, end = '.\n')
    else:
        print(digit, end = ', ')
print('Расчет долбоебов окончен.\n')

#вариант через генератор списков:
print('Расчет долбоебов через в квадратных скобках:')
digits = [digit+1 for digit in range (0, 20)]
print(digits)
print()


### 4.4. Миллион (шаг ограничиввает количество выводимых чисел).
numbers = list(range(0, 1_000_001, 100_000))
for number in numbers:
    print(number, end = ' ')
print()
print()


### 4.5. Суммирование миллиона чисел.
million = list(range(1,1_000_001))
print(f'Минимальное значение в списке: {min(million)}, максимальное: {max(million)}, сумма: {sum(million)}.')
print()


### 4.6. Нечетные числа.
print('Нечетные числа:')
odd_numbers = list(range(1,21,2))
for odd_number in odd_numbers:
    print(odd_number, end = ' ')
print()
print()


### 4.7. Тройки.
print('Числа, кратные трем:')
multiple_3_numbers = list(range(3,31,3))
for multiple_3_number in multiple_3_numbers:
    print(multiple_3_number, end = ' ')
print()
print()


### 4.8. Кубы.
print('Кубы чисел от 1 до 10:')
qube_numbers = list(range(1,11))
for qube_number in qube_numbers:
    if qube_number != 10:
        print(qube_number**3, end = ', ')
    else:
        print(qube_number**3, end = '.')
print()
print()


### 4.9. Генератор кубов.
print('Или, иными словами:')
qube_numbers_1 = [qube_number_1**3 for qube_number_1 in range (1, 11)]
print(qube_numbers_1)
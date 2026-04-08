print('\nВведите два числа, программа выведет результат деления.')
print('Введите "q" для выхода.\n')

while True:
    first_number = input('Первое число:\n')
    if first_number == 'q':
        break
    second_number = input('Второе число:\n')
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('На ноль делить нельзя! Введите числа заново\n')
    else:
        print(f'Результат деления: {answer}\n')
from name_function import get_formatted_name

print('\nДля выхода введите "q" в любое время.\n')

while True:
    first = input('Введите имя:\n')
    if first == 'q':
        break
    last = input('Введите фамилию:\n')
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print(f'\nПолное имя: {formatted_name}.\n')
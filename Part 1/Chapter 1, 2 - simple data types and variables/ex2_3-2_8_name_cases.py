    #2.3 Personal message
print('2.3 Персональной сообщение')

first_name = 'эРиК'
last_name = 'мЭтИз'

full_name = f'{first_name} {last_name}'

print(f'Здравствуйте, {full_name}, не хотите ли вы изучить Python сегодня?')
print()


#2.4 Регистр в символах и именах
print('2.4 Регистр в символах и именах')
#в нижнем регистре
print(f'Здравствуйте, {full_name.lower()}, не хотите ли изучить Python сегодня?')
#в верхнем регистре
print(f'Здравствуйте, {full_name.upper()}, не хотите ли изучить Python сегодня?')
#капитализация букв каждого слова
print(f'Здравствуйте, {full_name.title()}, не хотите ли изучить Python сегодня?')
print()


#2.5, 2.6 Знаменитая цитата с кавычками
print('2.5, 2.6 Знаменитая цитата с кавычками')
famous_person = 'альберт эйнштейн'
message = f'{famous_person.title()} однажды сказал: "Один, два, три"'
print(message)
print()


#2.7 удаление пробельных символов
print('2.7 удаление пробельных символов')
username = ' альберт эйнштейн \n\t'
print(f'Привет, {username}, как жизнь?')
print('clear')
username = username.strip()
username = username.title()
print(f'Привет, {username}, как жизнь?')
print()


#2.8 расширение файлов (преффиксы)
print('2.8 расширение файлов (преффиксы)')
filename = 'python_notes.txt'
print(filename)
filename = filename.removesuffix('.txt')
print(filename)
print()


#2.9 Число 8
print('2.9 число 8')
print(5 + 3)
print(11 - 3)
print(2 * 4)
print(80 / 10)
print()

#Любимое числа 24
first_name = 'лев'
last_name = 'константинов'
favorite_number = 24
print(f'Привет, {first_name.title()} {last_name.capitalize()}. Твое любимое число - {favorite_number}. Число в собственной степени = ', favorite_number ** favorite_number)
print()

import this
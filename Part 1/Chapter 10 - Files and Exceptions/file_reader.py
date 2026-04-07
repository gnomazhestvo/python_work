from pathlib import Path

path = Path('text_files/pi_million_digits.txt')

print('\nВывод информации "как есть":')
contents = path.read_text()
print(f"{contents[:52].rstrip()}...\n")

# Вывод информации из файла по строкам:
print('Вывод информации по строкам:')
lines = contents.splitlines()
pi_string =''

for line in lines:
    pi_string += line.lstrip()
print(f"{pi_string[:52]}...")
print(len(pi_string))

# Проверка есть ли в первом миллионе знаков числа пи комбинация
# цифр моей даты рождения 24.09.1996:
print('Есть ли дата рождения вашего рождения в числе пи?')
birthday = input('Давайте проверим. Введите ДР в формате ddmmyy:\n')
if birthday in pi_string:
    print('Да!')
else:
    print('Нет:(')

# Выведем 10 чисел перед ДР, ДР и 10 чисел после ДР:
index = pi_string.find('240996')
if index != -1:
    start = index - 10
    end = index + len(birthday) + 10
print(pi_string[start:end])
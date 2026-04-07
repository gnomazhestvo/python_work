# 10.4. Гость.
# Напишите программу, которая запрашивает у пользователя его
# имя. Введенный ответ сохраняется в файле guest.txt.
from pathlib import Path

print('10.4. Гость.\n')

path = Path('text_files/guest.txt')

name = input('Введите имя:\n')
path.write_text(name)
print('Имя успешно сохранено в text_files/guest.txt')
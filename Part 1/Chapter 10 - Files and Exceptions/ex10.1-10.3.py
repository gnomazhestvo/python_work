# 10.1. Изучение Python.
# Откройте пустой файл в текстовом редакторе и напишите
# несколько строк текста о возможностях Python. Каждая
# строка должна начинаться с фразы «В Python вы можете…».
# Сохраните файл под именем learning_python.txt в каталоге,
# использованном для примеров этой главы. Напишите программу,
# которая читает файл и выводит текст два раза: читая весь
# файл и сохраняя строки в списке, проходя по каждой строке.
from pathlib import Path

print('\n10.1. Изучение Python.\n')

path = Path('text_files/learning_python.txt')

# Выводит текст из файла, читая весь файл:
reading_text = path.read_text()
print(reading_text)

# Выводит текст из файла по строкам:
print()
lines = reading_text.splitlines()

# Создадим список для контроля регистра:
new_lines = []

# Цикл для изменения регистра на основании номера строки:
for i, line in enumerate(lines):
    if i == 0:
        new_line = line
        new_lines.append(new_line)
    else:
        new_line = line[0].lower() + line[1:]
        new_lines.append(new_line)

# Цикл для вывода с запятыми и точкой после последней строки:
for i in range(len(new_lines)):
    if i == len(new_lines)-1:
        print(f"{new_lines[i]}.")
    else:
        print(f"{new_lines[i]},", end=' ')

print('-- -- -- -- -- --\n')


# 10.2. Изучение C.
# Метод replace() может использоваться для замены любого
# слова в строке другим словом. В следующем примере слово
# 'dog' заменяется словом 'cat':
# 			>>> message = "I really like dogs."
# 			>>> message.replace('dog', 'cat')
# 			'I really like cats.'
# Прочитайте каждую строку из только что созданного файла
# learning_python.txt и замените слово Python названием
# другого языка — например, C. Выведите каждую измененную
# строку на экран.
print('10.2. Изучение C++\n')
for line in lines:
    new_line = line.replace('Python', 'C++')
    print(new_line)
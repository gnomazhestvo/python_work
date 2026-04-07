# 10.5. Гостевая книга. Напишите цикл while, который в
# цикле запрашивает у пользователей имена. При вводе каждого
# имени выведите на экран приветствие и добавьте строку с
# сообщением в файл guest_book.txt. Проследите за тем, чтобы
# каждое сообщение размещалось в отдельной строке файла.
from pathlib import Path

print('10.5. Гостевая книга.\n')

path = Path('text_files/guestbook.txt')
message_collect = ''
names = []

while True:
    name = input("Введите имя:\n(или введите 'q' для выхода)\n")
    if name != 'q':
        message = f"Добро пожаловать, {name.title()}! Вы записаны, проходите.\n"
        message_collect += message
        names.append(name)
        path.write_text(message_collect)
        print(message)
    else:
        print('\nСпасибо. Наши гости за сегодня:')
        for name in names:
            print(name.title())
        break
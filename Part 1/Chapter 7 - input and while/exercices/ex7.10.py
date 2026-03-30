# 7.10. Отпуск мечты.
# Напишите программу, которая опрашивает пользователей, где
# бы они хотели провести отпуск. Добавьте подсказку вида
# «Если бы вы могли посетить одно место в мире, то куда бы
# отправились?» Добавьте блок кода, который выводит результаты
# опроса.
print()
print('7.10. Отпуск мечты.')
print()

vacation_poll = {}

input_name_prompt = 'Как вас зовут?\n'
input_place_prompt = 'Если бы вы могли посетить одно место в мире,'
input_place_prompt += 'то куда бы вы отправились?\n'

print('Отпуск мечты.')

vacation_poll_active = True
while vacation_poll_active:
    name = input(input_name_prompt)
    if name.lower() == 'quit':
        break
    place = input(input_place_prompt)
    vacation_poll[name] = place

if vacation_poll:
    print('\n--- Результаты опроса ---')
    for name, place in vacation_poll.items():
        print(f'{name.title()} хотел бы поехать в {place.title()}')
else:
    print('Никто не принял участие в опросе.')
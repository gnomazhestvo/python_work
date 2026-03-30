# 7.8. Бутерброды.
# Создайте список sandwich_orders, заполните его названиями
# различных видов бутербродов. Создайте пустой список
# finished_sandwiches. В цикле переберите элементы первого
# списка и выведите сообщение для каждого элемента (например,
# «Я приготовил бутерброд с тунцом»). После этого каждый
# бутерброд из первого списка перемещается в список
# finished_sandwiches. После того как все элементы первого
# списка будут обработаны, выведите сообщение, в котором
# перечисляются все изготовленные бутерброды.
print()
print('7.8. Бутерброды.')

sandwich_orders = []

print('Сегодня готовим сэндвичи.')
prompt = 'Какой хотите?\n'
prompt += 'Когда завершите выбор, введите "stop"\n'

sandwiches_active = True
while sandwiches_active:
    new_sandwiche = input(prompt)
    sandwich_orders.append(new_sandwiche)
    if new_sandwiche == 'pastrami':
        sandwich_orders.pop()
        print('\nВНМИАНИЕ! к сожалению, пастромы сегодня нет в наличии.. выберите другой сэндвич.\n')
    if new_sandwiche == 'stop':
        sandwich_orders.pop()
        if len(sandwich_orders) <= 1:
            print('\nНи одного сэндвича не заказали... выберите хотя бы один.')
            continue
        else:
            break

print('\nВаш заказ принят.\nПРИСТУПАЕМ К ГОТОВКЕ\n')
finished_sandwiches = []

while sandwich_orders:
    preparing_sandwich = sandwich_orders.pop()   
    print(f'Сэндвич {preparing_sandwich} готовится...')
    print('--- three years later ---')
    print(f'Сэндвич {preparing_sandwich} готов!')
    finished_sandwiches.append(preparing_sandwich)
    print()
print(f'За сегодня приготовлены сэндвичи:')
for finished_sandwiche in finished_sandwiches:
    print(f'  - {finished_sandwiche}')
time = len(finished_sandwiches) * 3
print(f'Потрачено {time} лет.')
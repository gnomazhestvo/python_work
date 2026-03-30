# 7.4. Начинки для пиццы. Напишите цикл, который предлагает
# пользователю вводить начинки для пиццы до тех пор, пока не
# будет введено значение 'quit'. При вводе каждой начинки
# выведите сообщение о том, что она добавлена в заказ.
print('7.4. Начинки для пиццы.')
print()

toppings = []
prompt = '\nВведите начинку, которую желаете добавить:\n'
prompt += '(введите "quit", когда закончите.)\n'

active = True

while active:
    new_topping = input(prompt)
    if new_topping != 'quit':
        toppings.append(new_topping)
        print()
        print(f'{new_topping} - добавлено в пиццу.\n\nТекущий состав пиццы:')
        for topping in toppings:
            print(f'  - {topping}')
    else:
        active = False
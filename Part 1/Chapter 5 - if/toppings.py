requested_topping = 'mushrooms'
needed_topping = 'Anchovies'
if requested_topping != needed_topping:
    print(f'Hold the {needed_topping}!')

requested_toppings = ['mushrooms', 'onions', 'pineapple']

is_mushrooms_in_toppings = 'Mushrooms' in [requested_topping.lower() for requested_topping in requested_toppings]
print(is_mushrooms_in_toppings)

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print('Adding mushrooms')
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese')
print()

### Запись через цикл.
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping == 'green peppers':
            print('Sorry, we are out of green pepper:(')
        else:
            print(f'Adding {requested_topping}')
    print('Finished making your pizza!')
else:
    print('Are you sure you want eat pizza?')



### Множественный списки.
print('\nMaking new pizza!')
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print(f'Adding {requested_topping}')
        else:
            print(f'Sorry, {requested_topping} is unavailable for pizza... Chose another.')
else:
    print('Are you sure you want eat pizza?')
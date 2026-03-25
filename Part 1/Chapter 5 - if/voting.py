age = 19
print()
if age >= 18:
    print('You are old enough to vote!')
    print('Have you registered to the vote yet?')
else:
    print('Sorry, you are too young to vote.')
    print('Please register to vote as soon as you turn 18.')
print()

### Цепочки if-elif-else.
age = 65
if age <= 4:
    enter = 0
elif age < 18:
    enter = 25
elif age < 65:
    enter = 40
elif age >= 65:
    enter = 20
print(f'Your admission cost is ${enter}.')
print()

### Проверка нескольких условий.
requested_toppings = ['mushrooms', 'extra cheese']
print('Pizza:')
if 'mushrooms' in requested_toppings:
    print('  Adding mushrooms')
if 'pepperoni' in requested_toppings:
    print('  Adding pepperoni')
if 'extra cheese' in requested_toppings:
    print('  Adding extra cheese')
print('Finished making your pizza!')
### 4.10. Срезы.
print()
players = ['charles' ,'martina', 'michael', 'florence', 'eli']

print('Исходный список:')
print(players)
print()

print('Первые три пункта в списке - это:')
for player in players[0:3]:
    print(player.title())
print()

print('Три пункта из середины списка:')
for player in players[1:4]:
    print(player.title())
print()

print('Последние три пункта в списке - это:')
for player in players[-3:]:
    print(player.title())
print()


### 4.11. Моя пицца, твоя пицца.
my_pizzas = ['pepperoni', 'margarita', 'alfredo']
friend_pizzas = my_pizzas[:]

my_pizzas.insert(1, 'hunters')
friend_pizzas.insert(2, 'shitty')

print('Мои любимые пиццы:')
for my_pizza in my_pizzas:
    print(my_pizza.title())
print()

print('Любимые пиццы моего друга:')
for friend_pizza in friend_pizzas:
    print(friend_pizza.title())
print()


### 4.12. Больше циклов.
print()
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print('My favourite foods are:')
for my_food in my_foods:
    print(my_food.title())
print()

print("My friend's favourite foods are:")
for friend_food in friend_foods:
    print(friend_food.title())

print()

my_foods.append('canoli')
friend_foods.append('shit')
print('We have added some food to our lists.')
print('Now, my favourite foods are: ')
for my_food in my_foods:
    print(my_food.title())
print()

print("And my friend's:")
for friend_food in friend_foods:
    print(friend_food.title())
print()
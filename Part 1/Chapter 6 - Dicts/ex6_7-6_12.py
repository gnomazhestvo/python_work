# 6.7. Люди.
# Начните с программы, написанной для упражнения 6.1.
# Создайте два новых словаря, представляющих разных людей,
# и сохраните все три словаря в списке people. Переберите
# элементы списка людей. В процессе перебора выведите всю
# имеющуюся информацию о каждом человеке.
print()
print('6.7. Люди.')
print()

person_0 = {
    'first_name' : 'nastya',
    'last_name' : 'shkurina',
    'age' : 25,
    'city' : 'tyumen',
    'sex' : 'female'
    }
person_1 = {
    'first_name' : 'lev',
    'last_name' : 'konstantinov',
    'age' : 29,
    'city' : 'tyumen',
    'sex' : 'male'
}
person_2 = {
    'first_name' : 'boris',
    'last_name' : 'the cat',
    'age' : 6,
    'city' : 'yekaterinburg',
    'sex' : 'animal'
}

people = [person_0, person_1, person_2,]

for person in people:
    if person['sex'] == 'male':
        pronoun = 'He'
    elif person['sex'] == 'female':
        pronoun = 'She'
    else:
        pronoun = 'It'
    print(f"{person['first_name'].title()} {person['last_name'].title()}"
          f" is {person['age']} years being. {pronoun} lives in {person['city'].title()}.")
    print()
print()

# 6.8. Домашние животные.
# Создайте несколько словарей, имена
# которых представляют клички домашних животных. В каждом
# словаре сохраните информацию о виде животного и имени
# владельца. Сохраните словари в списке pets. Переберите
# элементы списка. В процессе перебора выведите всю имеющуюся
# информацию о каждом животном.
print('6.8. Домашние животные.')
print()

boris = {
    'name' : 'boris',
    'type' : 'cat',
    'age' : '6',
    'sex' : 'male',
    'owner' : 'lev',
    'location' : 'yekaterinburg',
}
rex = {
    'name' : 'rex',
    'type' : 'dog',
    'age' : '4',
    'sex' : 'male',
    'owner' : 'alex',
    'location' : 'sidelnikovo',
}
fogli = {
    'name' : 'fogli',
    'type' : 'turtle',
    'age' : '4',
    'sex' : 'female',
    'owner' : 'mom',
    'location' : 'pavlodar',
}

animals = [boris, rex, fogli,]

for animal in animals:
    name = animal.get('name', 'Unknown')
    print(name.title())

    for key, value in animal.items():
        if key == 'name':
            continue
        print(f'  {key.title()}: {value.title()}')
    print()
print()


# 6.9. Любимые места.
# Создайте словарь favorite_places. Придумайте названия трех
# мест, которые станут ключами словаря, и сохраните для
# каждого человека из упражнения 6.7 от одного до трех
# любимых мест. Чтобы задача стала более интересной, опросите
# нескольких друзей и соберите реальные данные для своей
# программы. Переберите данные в словаре, выведите имя
# каждого человека и его любимые места.
print('6.9. Любимые места.')
print()

person_0['favorite_places'] = ['sri-lanka', 'koffein', 'home']
person_1['favorite_places'] = ['tashkent', 'pavlodar', 'tyumen', 'svobodny']
person_2['favorite_places'] = ['toilet', 'trash']
for person in people:
    print(f'Favorite places of {person['first_name'].title()} {person['last_name'].title()}:')
    for favorite_place in person['favorite_places']:
        print(f'  {favorite_place.title()}')
    print()
print()

# 6.10. Любимые числа.
# Измените программу из упражнения 6.2, чтобы для каждого
# человека можно было хранить несколько любимых чисел.
# Выведите имя каждого человека в списке и его любимые числа.
print('6.10. Любимые числа.')
fav_nums = {
    'name_0' : ['11', '22', '63'],
    'name_1' : ['321', '123', '322', '66'],
    'name_2' : ['232'],
    'name_3' : ['55', '66', '777'],
    'name_4' : ['63', '43'],
    }
for name, nums in fav_nums.items():
        if len(nums) > 1:
            print(f'Любимые числа {name}:')
        else:
            print(f'Любимое число {name}:')
        for num in range(len(nums)):
            if num < len(nums) - 1:
                print(nums[num] + ', ', end = '')
            else:
                print(nums[num] + '.', end = '')
        print()
print()

# Задачка от гпт.
# Есть список. Вывести 'i like pizza, burger, pasta and sushi.
print('6.x1. Задачка от гпт.')
foods = ['pizza', 'burger', 'pasta', 'sushi']
print('I like', end = ' ')
for food_num in range(len(foods)):
    if food_num < len(foods) - 2:
        print(foods[food_num] + ', ', end = '')
    elif food_num == len(foods) - 2:
        print(foods[food_num] + ' and ', end = '')    
    else:
        print(foods[food_num] + '.', end = '')
print()
print()

# Задачка от гпт 2.
# Есть список. Нужно:
# 1.	Убрать дубликаты (одинаковые словари)
# 2.	Вывести:
# Alex (25) — доступ разрешен
# Ivan (17) — доступ запрещен
# Maria (30) — доступ разрешен
# Условия
# •	без set() (потому что там словари)
# •	использовать цикл
# •	age >= 18 → разрешен
print('6.x2. Задачка от гпт 2.')
print()

users = [
    {'name' : 'alex', 'age' : '25',},
    {'name' : 'ivan', 'age' : '17',},
    {'name' : 'maria', 'age' : '30',},
    {'name' : 'alex', 'age' : '25',},
]
unique_users = []

for user in users:
    if user not in unique_users:
        unique_users.append(user)
        if int(user['age']) >= 18:
            accesability = 'доступ разрешен'
        elif int(user['age']) < 18:
            accesability = 'доступ запрещен'
        else:
            accesability = 'error'
        print(f'{user['name'].title()} ({user['age']}) - {accesability}')
print()

# 6.11. Города.
# Создайте словарь cities. Используйте названия трех городов
# в качестве ключей словаря. Создайте словарь с информацией о
# каждом городе; добавьте в него страну, в которой расположен
# город, примерную численность населения и один примечательный
# факт, относящийся к этому городу. Ключи словаря каждого
# города должны называться country, population и fact.
# Выведите название каждого города и всю сохраненную
# информацию о нем.
print('6.11. Города.')
print()
cities = {
    'gotham' : {
        'country' : 'USA',
        'population' : 100_000,
        'fact' : 'Batman lives here',
    },
    'pavlodar' : {
        'contry' : 'Kazakhstan',
        'population' : 300_000,
        'fact' : 'Skryptonite from this city',
    },
    'tashkent' : {
        'country' : 'Uzbekistan',
        'populatiin' : 3_000_000,
        'fact' : 'funny'
    },
}
for city, city_infos in cities.items():
    print(city.title())
    for city_infos_key, city_infos_value in city_infos.items():
        print(f"{city_infos_key.title()}: {city_infos_value}")
    print()
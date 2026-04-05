import random

random_num = random.randint(1, 3)
print(f'Случайное число в диапазоне от 1 до 3: {random_num}.\n')

players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = random.choice(players).title()
print('Список игроков:')
for player in players:
    print(f"- {player.title()}")
print(f'Первым будет ходить {first_up}')
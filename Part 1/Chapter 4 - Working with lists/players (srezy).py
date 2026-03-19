players = ['charles' ,'martina', 'michael', 'florence', 'eli']
print(players)
print(players[0:3])
print(players[1:4])

print(players[:2])
print(players[:-2])
print(players[-2:])

print(players[1:4:8])
print()

print('Трое игроков моей команды:')
for player in players[0:3]:
    print(player.title())
print()

print('Первые трое игроков моей команды по алфавиту:')
players = sorted(players)
for player in players[0:3]:
    print(player.title())
print()
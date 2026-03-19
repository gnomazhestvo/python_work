#3.1 Имена.
print()
names = ['nastya', 'alex', 'fred', 'arnold']
names = [name.title() for name in names]
print('Ниже список моих друзей:\n\t', names[0], '\n\t', names[1], '\n\t', names[2], '\n\t', names[3])
print()

#3.2 Сообщения
names = [name.upper() for name in names]
message_for_nastya = f'Привет, любимая {names[0]}'
message_for_alex = f'Добро пожаловать на сервер, {names[1]}'
message_for_fred = f'{names[2].title()} Perry'
message_for_arnold = f'hey, {names[-1]}'
print(message_for_nastya)
print(message_for_alex)
print(message_for_fred)
print(message_for_arnold)
print()

#3.3 Собственный список
autos = ['Mercedes-Benz', 'audi', 'BMW', 'Honda', 'Toyota']
autos = [auto.upper() for auto in autos]
print (f'{autos[0]} и {autos[1]} - хорошие автомобили, но')
print(f'я бы хотел купить мотоцикл {autos[3].title()}')
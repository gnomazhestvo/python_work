message = 'Enter a number, and I will tell if it is even or odd:\n'
number = input(message)
number = int(number)

if number % 2 == 0:
    print('even')
elif number % 2 != 0:
    print('odd')
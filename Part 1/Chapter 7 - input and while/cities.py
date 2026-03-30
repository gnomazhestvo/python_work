prompt = '\nPlease enter the name of a city you have visited:'
prompt += '\n(Enter "quit" when you ave finished.)\n'

while True:
    city = input(prompt)
    if city == 'quit':
        quit_logo = input('Are you sure?\n')
        if quit_logo.lower() == 'yes' or quit_logo.lower() == 'y':
            break
        else:
            continue
    else:
        print(f'I would love to go to {city.title()}')

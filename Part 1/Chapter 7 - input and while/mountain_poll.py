responses = {}

polling_active = True

while polling_active:
    name = input('\nEnter your name or QUIT to finish:\n')
    if name.lower() == 'quit':
        polling_active = False
        
        continue


while polling_active:
    name = input('\nEnter your name or QUIT to finish:\n')
    if name.lower() == 'quit':
        break
    response = input('\nWhich mountain do you like the most?\n')
    responses[name] = response

if responses:
    print('\n---Polling results---')
    for name, response in responses.items():
        print(f'{name.title()} wants to go to {response}')
else:
    print('No results.')
prompt = 'Tell me something, and I will repeat it back to you.\n'
prompt += 'Or input "quit" to close the programm: \n'

active = True

while active:
    message = input(prompt)
    if message != 'quit':
        print(message)
    else:
        active = False
    print()
print()
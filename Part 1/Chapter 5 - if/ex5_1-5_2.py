### 5.1. Проверка условий.
print(1)
car = 'subaru'
print('Is car Subaru? I predict True.')
print(car == 'subaru')
print()

print(2)
print('Is car - Audi? I predict False.')
print(car == 'Audi')
print()

### 5.2. Больше проверок условий.

## 5.2.3
print('3. Проверка равенства и неравенства строк')
string_1 = 'hello'
string_2 = 'world'
string_3 = 'hello'
string_4 = 'world'
print(string_1 == string_2)
print(string_1 == string_2 or string_1 == string_3)
print(string_1 == string_3 and string_2 == string_4)
print()

## 5.2.4
print('4. Проверка с использованием метода .lower()')
asses = ['Andrew', 'bootie', 'momnster', 'SKRILLEX']
bsses = ['MAtthew', 'carolina', 'worldo', 'skrillex', 'momnster', 'bootie', 'nastya', 'ccc', 'Borrido']

for bss in bsses:
    print(f'Is {bss.title()} in origin list?', end = ' ')
    print(bss.lower() in [ass.lower() for ass in asses])
    print()

## 5.2.5
print('5. Проверка вхождения элемента в список.')
print('6. Проверка отсутствия элемента в списке.')
list = ['a', 'b', 'h', 'g', 'f', 'y', 'w', 'o']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i' , 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for every_symbol in alphabet:
    print(every_symbol, ': ', end = ' ')
    if every_symbol in list:
        print('Yes')
    else:
        print('No')
print('thx')
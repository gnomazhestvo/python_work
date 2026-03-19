### 3.8 Повидать мир.
print()
countries = ['Japan', 'Russia', 'Armenia', 'Vietnam', 'Thai-Land']
print('Default list: ', countries)

#обычная временная сортировка:
print('Sorted list: ', sorted(countries))

#доказательство временности сортировки:
print('Default list again: ', countries)

#сортировка в обратном алфавитном порядке:
print('Alphabetly reversed list: ', sorted(countries, reverse = True))

#снова доказательство временности сортировки:
print('Default list again and again: ', countries)

#использование метода .reverse:
countries.reverse()
print('The reverse listed list: ', countries)

#повторный reverse() выдает изначальный список:
countries.reverse()
print('Double reverse gives default list: ', countries)

#сортировка с помощью sort():
countries.sort()
print('List is foreverely sorted: ', countries)

#обратная сортировка с помощью sort():
countries.sort(reverse = True)
print('Alphabetly reversed foreverely sorted list: ', countries)
print()
print('===')
print()


### 3.9 Количество гостей
guests = ['Альберт Эйнштейн', 'Арнольд Эй', 'Лил Нэсти', 'Кот Борис', 'Мерседес Бенз', 'Алексей Константинов', 'Матвей Андреев']
print('К сожалению, только что выяснилось, что новый обеденный стол будет доставлен позже обеда. Необходимо вновь пересмотреть список приглашений. Максимальное число гостей - двое. На текущий момент количество гостей - ', len(guests), '.\n')
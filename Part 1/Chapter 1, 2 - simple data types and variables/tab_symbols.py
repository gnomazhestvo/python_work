# next_string_operand = '\n'
# tab_operand = '\t'


print()
print('Python')

print('\nPython')

print('\tPython\n')

print('Languages:\n\tPython\n\tC\n\tJavaScript')

#удаление лишних пробелов слева, справа, с обеих сторон
favorite_language = 'Python'
favorite_language_1 = 'Python '
check = favorite_language == favorite_language_1
check_with_rstrip = favorite_language.rstrip() == favorite_language_1.rstrip()
print(check)
print(check_with_rstrip)

#удаление префиксов
nostarch_url = 'https://nostarch.com'
simple_url = nostarch_url.removeprefix('https://')
print(simple_url)
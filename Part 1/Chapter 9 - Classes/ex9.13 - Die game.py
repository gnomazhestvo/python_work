# 9.13. Игра в кости.
# Создайте класс Die с одним атрибутом sides, который
# имеет значение по умолчанию 6. Напишите метод roll_die()
# для вывода случайного числа от 1 до количества граней на
# кубике. Создайте экземпляр, представляющий шестигранный
# кубик, и смоделируйте десять бросков.
# 
# Создайте экземпляры, представляющие 10- и 20-гранный кубик.
# Смоделируйте десять бросков каждого кубика.

from random import randint

class Die:
    """Описывает модель кубика."""

    def __init__(self, sides=6):
        """Инициализация атрибутов."""
        self.sides = sides
    
    def roll_die(self):
        """Бросок кубика"""
        result = randint(1, self.sides)
        return result


# Экземпляр шестигранного кубика
six_sides_die = Die()

# Результат десяти бросков шестигранного кубика:
results = [six_sides_die.roll_die() for _ in range (11)]
print(f"Результаты бросков {six_sides_die.sides}-гранного кубика:")
print(results)

print('\n== == == ==\n')


# Экземпляр 10-гранного кубика
ten_sides_die = Die(10)

# Результат десяти бросков 10-гранного кубика:
results = [ten_sides_die.roll_die() for _ in range (11)]
print(f"Результаты бросков {ten_sides_die.sides}-гранного кубика:")
print(results)

print('\n== == == ==\n')


# Экземпляр 20-гранного кубика
twenty_sides_die = Die(20)

# Результат десяти бросков 10-гранного кубика:
results = [twenty_sides_die.roll_die() for _ in range (11)]
print(f"Результаты бросков {twenty_sides_die.sides}-гранного кубика:")
print(results)
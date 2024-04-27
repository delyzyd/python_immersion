"""
Добавьте в модуль с загадками функцию, которая
 принимает на вход строку (текст загадки) и
 число (номер попытки, с которой она угадана).
  Функция формирует словарь с информацией о
  результатах отгадывания. Для хранения
  используйте защищённый словарь уровня модуля.
Отдельно напишите функцию, которая выводит
результаты угадывания из защищённого словаря
в удобном для чтения виде. Для формирования
результатов используйте генераторное выражение.
"""
from riddles1 import secrets

_data = {}


def storage():
    puzzles = {
        'Зимой и летом одним цветом': ['ель', 'ёлка', 'сосна'],
        'Не лает, не кусает, в дом не пускает': ['замок'],
        'Сидит дед во сто шуб одет': ['лук', 'луковица'],
    }
    for key, value in puzzles.items():
        result = secrets(key, value)
        print(f'Угадал с {result} попытки' if result > 0 else 'Не угадал')
        yield key, result


def save(puzzle: str, count: int):
    _data.update({puzzle: count})


def show():
    res = (f'Загадку "{key}" разгадали с {value}-й попытки' if value > 0
           else f'Загадку "{key}" не разгадали'
           for key, value in _data.items())
    print('\n'.join(res))


if __name__ == '__main__':
    generator = storage()
    for key, result in generator:
        save(key, result)
    show()

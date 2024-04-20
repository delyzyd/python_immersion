# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.*Верните все возможные варианты комплектации рюкзака.

from itertools import combinations

def all_valid_combinations(items, max_weight):
    # Список для хранения всех допустимых комбинаций
    valid_combinations = []


    for r in range(1, len(items) + 1):
        for combo in combinations(items.items(), r):
            total_weight = sum(item[1] for item in combo)

          
            if total_weight <= max_weight:
                valid_combinations.append({item[0]: item[1] for item in combo})

    return valid_combinations

items = {
    "Палатка": 4.5,
    "Котелок": 1.0,
    "Спальник": 3.2,
    "Фонарик": 0.5,
    "Питание": 2.0,
    "Вода": 3.0
}

# Максимальная грузоподъёмность рюкзака
max_weight = 10

# Получение всех возможных допустимых комбинаций
valid_combinations = all_valid_combinations(items, max_weight)
print("Все возможные комбинации предметов:")
for i, combo in enumerate(valid_combinations, 1):
    print(f"Комбинация {i}: {combo}, Суммарный вес: {sum(combo.values())}")
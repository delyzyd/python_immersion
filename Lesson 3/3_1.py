# Урок 3. Коллекции

# Задача 2. Дан список повторяющихся элементов. 
# Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

from collections import Counter

def find_duplicates(input_list):
    element_count = Counter(input_list)
    duplicates_list = [item for item, count in element_count.items() if count > 1]
    
    return duplicates_list
# Пример использования функции
input_list = [1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 7,6,6,5,8,8,9,9,9,9]
result = find_duplicates(input_list)
print(result)
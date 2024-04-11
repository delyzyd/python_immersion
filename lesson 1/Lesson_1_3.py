# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)
from random import randint

# Задаем границы для загадываемого числа
LOWER_LIMIT = 0
UPPER_LIMIT = 1000

# Генерируем случайное число
num = randint(LOWER_LIMIT, UPPER_LIMIT)

turne = 10

print("Программа загадала число от 0 до 1000. Попробуй угадать это число за 10 попыток.")

# Цикл попыток угадать число
while turne > 0:
    try:
        # Получаем ввод от пользователя
        a = int(input("Введи число: "))
        if a < LOWER_LIMIT or a > UPPER_LIMIT:
            print(f"Число должно быть в пределах от {LOWER_LIMIT} до {UPPER_LIMIT}. Попробуйте еще раз.")
            continue
        
        # Проверяем, угадал ли пользователь число
        if a == num:
            print("Поздравляем, ты угадал число!")
            break
        elif a < num:
            print("Больше")
        else:
            print("Меньше")
        
        turne -= 1
        print(f"Осталось попыток: {turne}")
        
    except ValueError:
        print("Пожалуйста, вводите только целые числа.")
        continue

# Если попытки закончились
if turne == 0:
    print(f"Попытки закончились. Загаданное число было: {num}")
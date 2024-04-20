# Создайте функцию генератор чисел Фибоначчи

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
iterr = int(input('Введите число последовательностей: '))
# Пример использования:
fib_gen = fibonacci()
for _ in range(iterr):  # Выведем первые 10 чисел Фибоначчи
    print(next(fib_gen))
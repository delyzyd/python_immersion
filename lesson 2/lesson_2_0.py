# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

def dec_to_hex(n):
    hex_chars = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 
                 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    hex_str = "" 
    if n < 0: 
        n += 2**32
    while n > 0:
        hex_str = hex_chars[n % 16] + hex_str
        n = n // 16
    return "0x" + hex_str if hex_str else "0x0"

try:
    number = int(input("Введите целое число: "))
    hex_representation = dec_to_hex(number)
    print(f"Шестнадцатеричное представление (вручную): {hex_representation}")
    print(f"Проверка с hex: {hex(number)}")
    assert(hex_representation == hex(number)), "Результаты не совпадают"
except ValueError:
    print("Пожалуйста, введите корректное целое число.")
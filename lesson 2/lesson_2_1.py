# 2. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions


from fractions import Fraction

def sum_and_product_of_fractions(frac1_str, frac2_str):
    frac1 = Fraction(frac1_str)
    frac2 = Fraction(frac2_str)
    
   
    sum_result = frac1 + frac2
    product_result = frac1 * frac2
    
    return sum_result, product_result


frac1_str = input("Введите первую дробь в формате a/b: ")
frac2_str = input("Введите вторую дробь в формате a/b: ")

sum_result, product_result = sum_and_product_of_fractions(frac1_str, frac2_str)

print(f"Сумма дробей: {sum_result}")
print(f"Произведение дробей: {product_result}")
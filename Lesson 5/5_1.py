# Урок 5. Итераторы и генераторы
# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
import os

def parse_file_path(file_path):
    # Получаем путь до папки и полное имя файла
    directory, filename = os.path.split(file_path)
    # Разделяем имя файла на имя и расширение
    name, extension = os.path.splitext(filename)
    
    # Возвращаем кортеж
    return (directory, name, extension)

# Пример использования
file_path = "/path/to/your/folder/example.txt"
result = parse_file_path(file_path)
print(result)  
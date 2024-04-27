'''Напишите функцию группового переименования файлов. Она должна:
a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] 
берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. 
Далее счётчик файлов и расширение'''

import os

def group_rename_files(desired_name, num_digits, original_extension, new_extension, range_name=None):
    file_counter = 1
    for filename in os.listdir('.'):
        if filename.endswith(original_extension):
            if range_name:
                original_name = filename[range_name[0]:range_name[1]]
            else:
                original_name = filename[:filename.index(original_extension)]
            new_name = f'{original_name}_{desired_name}_{str(file_counter).zfill(num_digits)}.{new_extension}'
            os.rename(filename, new_name)
            file_counter += 1


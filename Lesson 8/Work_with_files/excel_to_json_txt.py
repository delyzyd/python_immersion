''' Функция по работе с excel и переводом в txt и json форматы'''


import pandas as pd

def excel_to_txt_and_json(excel_file, txt_filename, json_filename):
    # Загрузить Excel файл в DataFrame
    df = pd.read_excel(excel_file)# Задайте путь к файлу и не забудте ковычки и знак r

    # Сохранить данные из DataFrame в текстовый файл
    with open(txt_filename, 'w') as f:
        for index, row in df.iterrows():
            f.write(row.to_string() + '\n')  # Каждая строка DataFrame преобразуется в строку и записывается в файл
            f.write('\n')  # Добавить пустую строку между записями для лучшей читаемости

    # Сохранить данные из DataFrame в JSON файл
    df.to_json(json_filename, force_ascii=False, indent=4)

# Пример использования
excel_file_path = 'example.xlsx'
txt_output_path = 'output.txt'
json_output_path = 'output.json'

excel_to_txt_and_json(excel_file_path, txt_output_path, json_output_path)
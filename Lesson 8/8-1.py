'''Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. 
Результаты обхода сохраните в файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных
файлов и директорий.'''

import os
import json
import csv
import pickle
import pandas as pd

def dir_size(path):
    total = 0
    for entry in os.scandir(path):
        if entry.is_file():
            total += entry.stat().st_size
        elif entry.is_dir():
            total += dir_size(entry.path)
    return total

def recursive_scandir(path, parent=None):
    result = []
    try:
        for entry in os.scandir(path):
            item = {
                "name": entry.name,
                "parent": parent,
                "type": "directory" if entry.is_dir() else "file",
                "size": dir_size(entry.path) if entry.is_dir() else entry.stat().st_size,
            }
            result.append(item)
            if entry.is_dir():
                result.extend(recursive_scandir(entry.path, entry.path))
    except PermissionError:
        print(f"Permission denied: {path}")
    return result

def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def save_to_csv(data, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "parent", "type", "size"])
        writer.writeheader()
        writer.writerows(data)

def save_to_pickle(data, filename):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

def save_to_excel(data, filename):
    df = pd.DataFrame(data)
    df.to_excel(filename + '.xlsx', index=False)

def export_directory_data(dir_path, output_dir=None):
    if output_dir is None:
        output_dir = dir_path
    else:
        os.makedirs(output_dir, exist_ok=True)
        
    data = recursive_scandir(dir_path)
    base_filename = os.path.join(output_dir, os.path.basename(dir_path.rstrip(os.sep)))

    save_to_json(data, base_filename + '_data.json')
    save_to_csv(data, base_filename + '_data.csv')
    save_to_pickle(data, base_filename + '_data.pickle')
    save_to_excel(data, base_filename + '_data')

directory_to_scan = r'C:\Users\Asus\Desktop\Учеба\Geekbrains\python погружение'
output_directory = r'C:\Users\Asus\Desktop\Учеба\Geekbrains\python погружение'
export_directory_data(directory_to_scan, output_directory)
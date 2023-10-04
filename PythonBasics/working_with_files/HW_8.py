# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и 
# все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с 
# учётом всех вложенных файлов и директорий. 3.Соберите из созданных на уроке и в 
# рамках домашнего задания функций пакет для работы с файлами разных форматов.
import os
from pathlib import Path
import json
import pickle
import csv

__all__ = ['HW_8'] 

def HW_8(path: str = Path.cwd()):
    
    path_contents_dict = {}

    for path, directories, files in os.walk(path):
        
        for directory in directories:
            dir_obj = Path(path)
            directory_name = directory
            parent_folder = dir_obj.name
            file_count = len(list(dir_obj.glob('*')))
            path_contents_dict[directory_name] = {'type':'directory', 'parent_folder':parent_folder, 'size':file_count}
        for file in files:
            file_name = file
            file_path = Path(path) / file
            file_size_bytes = file_path.stat().st_size
            path_contents_dict[file_name] = {'type':'file', 'parent_folder':parent_folder, 'size':file_size_bytes}
        
        #Converting path_contents_dict to json
        with open('path_contents.json', 'w', encoding='utf-8') as json_f:
            json.dump(path_contents_dict, json_f, ensure_ascii=False, indent=2)

        #Converting path_contents_dict to pickle
        with open('path_contents.pickle', 'wb') as pickle_f:
            pickle.dump(path_contents_dict, pickle_f, protocol=pickle.DEFAULT_PROTOCOL)

        #Converting path_contents_dict to csv
        with open('path_contents.csv', 'w', newline='') as csv_f:
            csv_writer = csv.DictWriter(csv_f, fieldnames=['object_name','type', 'parent_folder', 'size'])
            csv_writer.writeheader()
            for object_name, object_info in path_contents_dict.items():
                csv_writer.writerow({'object_name':object_name, 'type':object_info['type'], 'parent_folder':object_info['parent_folder'], 'size':object_info['size']})

if __name__ == '__main__':
    HW_8()
# 📌Напишите функцию, которая ищет json файлы в указанной директории и сохраняет 
# их содержимое в виде одноимённых pickle файлов.
import os
from pathlib import Path
import json
import pickle

__all__ = ['json_to_pickle']

def json_to_pickle(path: str = Path.cwd()):
    for path, directories, files in os.walk(path):
        for file in files:
            file_obj = Path(file)
            if file_obj.suffix == '.json':
                with(
                    open(f"{file_obj.name.replace('.json', '')}.pickle", 'wb') as pickle_f,
                    open(f'{file_obj.resolve()}') as json_f,
                ):
                    json_dict = json.load(json_f)
                    pickle.dump(json_dict, pickle_f, protocol=pickle.DEFAULT_PROTOCOL)

if __name__ == '__main__':
    json_to_pickle()
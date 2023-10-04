# 📌Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader. 
# 📌Дополните id до 10 цифр незначащими нулями. 
# 📌В именах первую букву сделайте прописной. 
# 📌Добавьте поле хеш на основе имени и идентификатора. 
# 📌Получившиеся записи сохраните в json файл, где каждая строка csv файла 
# представлена как отдельный json словарь. 
# 📌Имя исходного и конечного файлов передавайте как аргументы функции.

import csv
import json

__all__ = ['csv_to_json']

def csv_to_json():
    
    final_dict = {}

    with open('json_to_csv.csv', 'r', encoding='utf-8') as csv_f:
        csv_list = list(csv.reader(csv_f))
        csv_list = csv_list[1:]
    for item in csv_list:
        item[1] = item[1].zfill(10)
        item[2] = item[2].capitalize()
        item.append(hash(item[1]+item[2]))
        final_dict[item[3]]=item
    with open('csv_to_json.json','w+', encoding='utf-8') as json_f:
        json.dump(final_dict, json_f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    csv_to_json()
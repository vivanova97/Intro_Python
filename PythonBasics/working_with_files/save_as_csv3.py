# Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.

import csv, json

__all__ = ['convert_to_csv']

def load_json_file():
    with open('users.json', 'r', encoding='utf-8') as json_f:
        json_file_dict = json.load(json_f)
        print(json_file_dict)
        return json_file_dict

def convert_to_csv():
    json_file_dict = load_json_file()
    with open('json_to_csv.csv','w+', encoding='utf-8', newline='') as csv_f:
        csv_write_obj = csv.DictWriter(csv_f, fieldnames=['permission_level', 'id', 'name'])
        csv_write_obj.writeheader()
        for permission_lvl, ids in json_file_dict.items():
            for id, name in ids.items():
                csv_write_obj.writerow({"permission_level":permission_lvl,"id":id,"name":name})

if __name__ == '__main__':
    convert_to_csv()
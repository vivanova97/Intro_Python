# Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи
# 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков
# столбца из переданного файла.

import pickle, csv

__all__ = ['pickle_to_csv']

def pickle_to_csv():
    with(
        open('users.pickle', 'rb') as pickle_f,
        open('pickle_to_csv.csv', 'w+', encoding='utf-8') as csv_f
    ):
        pickle_dict = pickle.load(pickle_f)
        csv_obj = csv.DictWriter(csv_f, fieldnames=['permission_level', 'id', 'name'])
        csv_obj.writeheader()
        for permission_level, users in pickle_dict.items():
            for user_id, name in users.items():
                csv_obj.writerow({'permission_level':permission_level,'id':user_id,'name':name})

if __name__ == '__main__':
    pickle_to_csv()
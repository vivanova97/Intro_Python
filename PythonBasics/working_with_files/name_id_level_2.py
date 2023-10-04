# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор 
# и уровень доступа (от 1 до 7). 📌После каждого ввода добавляйте новую информацию в 
# JSON файл. 📌Пользователи группируются по уровню доступа. 
# 📌Идентификатор пользователя выступает ключём для имени. 
# 📌Убедитесь, что все идентификаторы уникальны независимо от уровня доступа. 
# 📌При перезапуске функции уже записанные в файл данные должны сохраняться.

import json

__all__ = ['main_program']

def load_json_file():
    try:
        with open('users.json','r',encoding='utf-8') as json_file:
                user_dict = json.load(json_file)
    except json.decoder.JSONDecodeError:
        user_dict = {}
    
    return user_dict 


def get_info():
    name = input('Enter your name: ')
    while True:
        try:
            person_id = input('Enter your id: ')
            if not person_id.isdigit() or len(person_id) != 7:
                raise ValueError('ID should be 7 digits.')
            else:
                for permission_level, ids in user_dict.items():
                    if int(person_id) in ids:
                        raise ValueError('Person with this ID already exists.')
                person_id = int(person_id)
                break
        except ValueError as e:
            print(f'Error: {e}')
    while True:
        try:
            permission_level = input(f'Enter permissions level: ')
            if not permission_level.isdigit() or (0 > int(permission_level) > 7):
                raise ValueError('Enter a permission level from 1-7.')
            else:
                permission_level = int(permission_level)
                break
        except ValueError as e:
            print(f'Error: {e}')
    
    return name, person_id, permission_level


def update_user_dict():
    name, person_id, permission_level = get_info()
    
    if f'{permission_level}' not in user_dict:
        user_dict[f'{permission_level}'] = {person_id:name}
    else:
        user_dict[f'{permission_level}'][person_id] = name


def update_json_file():
    with open('users.json', 'w+', encoding='utf-8') as json_file:
        json.dump(user_dict, json_file, indent=2)

def main_program():
        while True:
            global user_dict
            user_dict = load_json_file()
            update_user_dict()
            update_json_file()

if __name__ == '__main__':
    main_program()

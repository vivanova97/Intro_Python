import pandas as pd
import pprint

def show_menu():
    print("\nВыберите необходимое действие:\n"
    "1. Отобразить весь справочник\n"
    "2. Найти абонента по имени или фамилии\n"
    "3. Найти абонента по номеру телефона\n"
    "4. Добавить абонента в справочник\n"
    "5. Редактировать данные абонента в справочнике\n"
    "6. Удалить абонента из справочника\n"
    "7. Сохранить справочник в текстовом формате\n"
    "8. Закончить работу")
    choice = int(input("Ваш выбор: "))
    return choice

def get_phone_book(filename):
    df = pd.read_csv(filename)
    records = df.to_dict('records')
    return [dict(zip(df.columns, record.values())) for record in records]

def add_person():
    data = open('seminar8_phonebook.txt', mode= 'a', encoding='utf-8')
    last_name = input('Enter the last name of the person:')
    first_name = input('Enter the first name of the person:')
    phone = input('Enter the phone number: ')
    description = input('Short description: ')
    data.write(f'{last_name}, {first_name}, {phone}, {description} \n')
    data.close()

def replace_data_phonebook(old_value, new_value):
    df = pd.read_csv("seminar8_phonebook.csv")
    df.replace(old_value, new_value, inplace=True)
    df.to_csv("seminar8_phonebook.csv", index=False)

def delete_person():
    phone = input("Enter the phone number of the person to delete: ")
    df = pd.read_csv("seminar8_phonebook.csv", sep = ',')
    df = df[df["phone"] != phone]
    df.to_csv("seminar8_phonebook.csv", index=False)
    print("Person deleted successfully.")

def create_txt_phonebook():
    data = open('seminar8_phonebook.csv', mode='r', encoding='utf-8')
    txt_list = list(data)
    data2 = open('seminar8_phonebook.txt', mode='w', encoding= 'utf-8')
    data2.writelines(txt_list)
    
def work_with_phonebook():
    choice = show_menu()
    phone_book = get_phone_book('seminar8_phonebook.csv')
    while (choice != 8):
        if choice == 1:
            for person in phone_book:
                print(person)
        elif choice == 2:
            name = input("Input name: ")
            for person in phone_book:
                if person["first_name"] == name:
                    print(person)
        elif choice == 3:
            phone = input("Input phone number: ")
            for person in phone_book:
                if person["phone"] == phone:
                    print(person)
        elif choice == 4:
            add_person()
        elif choice == 5:
            phone = int(input(f'Enter the phone number of the person: '))
            criteria = input(f"What would you like to change? Type: 'last name', 'first name', 'phone' or 'description': ")
            change = input(f'What should the new {criteria} be? Type here: ')
            for person in phone_book:
                if person['phone'] == phone:
                    old_value = person[criteria] 
                    person[criteria] = change
                    print(old_value, change)
                    pprint.pprint(person)
                    replace_data_phonebook(old_value, change)
                    break
        elif choice == 6:
            delete_person()
        elif choice == 7:
            create_txt_phonebook()
        choice = show_menu()
        if choice == 8:
            print("Thank you for contacting the phonebook!")
            break


def var_dump(data):
    if isinstance(data, dict):
        print("array(")
        for key, value in data.items():
            print(f"  [{key}] => {type(value).__name__}")
            var_dump(value)
        print(")")
    elif isinstance(data, list):
        print("array[")
        for item in data:
            print(f"  {type(item).__name__}")
            var_dump(item)
        print("]")




df = pd.read_csv('seminar8_phonebook.csv')
print(type(df))
def print_odd_lines():
    object1 = open('practice4.txt')
    text = object1.readlines()
    object1.close()
    for line_num in range(0,len(text),2):
            print(text[line_num])

def print_even_lines():
    object1 = open('practice4.txt')
    text = object1.readlines()
    object1.close()
    for line_num in range(1,len(text),2):
            print(text[line_num])

    
def order_practice4_1():
    object1 = open('practice4_1.txt')
    list1 = object1.read().split(' ')
    object1.close()
    price_list = []
    item_list = []
    for item in list1:
            if item.isnumeric() == True:
                price_list.append(int(item))
            else: item_list.append(item)
    print(item_list)
    print(price_list)
    item_price_list = dict(zip(item_list, price_list))
    print(item_price_list)

def generate_random_password():
    import random
    object1 = open('practice4_2.txt',encoding='utf-8')
    symbols = object1.read()
    object1.close()
    password_for = input('Enter which application the password is for: ')
    desired_password_length = int(input('Enter the password length: '))
    password = str()
    for i in range(0,desired_password_length):
        random_index = random.randint(0, len(symbols)-1)
        password += symbols[random_index]
    data = open('passwords.txt', mode='a', encoding='utf-8')
    data.writelines(f'{password_for}: {password} \n')
    data.close()


generate_random_password()





#Задача 30:  Заполните массив элементами арифметической прогрессии. 
#Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
#Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
#Каждое число вводится с новой строки.
def problem30():
    list = [int(input('Enter the first element:'))]
    number_of_elements = int(input('Enter the number of elements in list:'))
    difference = int(input('Enter the difference between elements:'))


    for i in range(1, number_of_elements):
        list.insert(i, list[i-1] + difference)
    print(list)


#Задача 32: Определить индексы элементов массива (списка), значения которых 
#принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше 
#заданного максимума)
def random_list(start_number, end_number, list_size):
    import random
    return [random.randint(start_number,end_number+1) for i in range(list_size)]
    
def problem32():
    list = random_list(1,100,10)

    print(f'The list created is : {list}')

    min_num = int(input('Enter the min number in range: '))
    max_num = int(input('Enter the max number in range: '))

    print(f'The indexes within {min_num} and {max_num} are: ', end = '')
    for i in range(len(list)):
        if list[i] >= min_num and list[i] <= max_num:
            print(f'{i} ', end='') 
    print()
problem32()
#Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
#Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
#m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

def problem1():
    from Practice3 import quick_sort

    list1_length = int(input('Enter the length of first list: '))
    list2_length = int(input('Enter the length of second list: '))

    list1 = []
    list2 = []


    for item in range(list1_length):
        list1.append(int(input(f'Enter {item+1} number in list:')))


    for item in range(list2_length):
        list2.append(int(input(f'Enter {item} number in list:')))

    list1 = set(list1)
    list2 = set(list2)

    list3 = list1.intersection()

    quick_sort(list(list3))

    print(list3)


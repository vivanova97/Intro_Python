#Напишите программу, которая принимает на вход число N 
#и выдает список факториалов для чисел от 1 до N.
def problem1():
    factorial = 1
    number = int(input('Enter a number: '))
    if number == 0:
        print(f'0! = 1')
    else:
        for i in range(1,number):
            factorial*=i
            print(f'{i}! factorial = {factorial}')

#Выведите таблицу истинности для выражения -(XAM)VZ.
def problem2():
    print(f'X M Z -(XAM)VZ')
    for X in range(0,2):
        for M in range (0,2):
            for Z in range (0,2):
                print(f'{X} {M} {Z} {not{X and M} or Z}')

#Задайте список из N елементов, заполненных числами из промежутка [-N, N]. 
#Сдвиньте все элементы списка на 2 позиции вправо.
def problem3_using_pop_and_insert():
    N = abs(int(input("Enter a number:")))

    list_N = []

    for i in range(-N,N+1):
        list_N.append(i)
    print(list_N)

    list_N.insert(0,list_N.pop(-2))
    list_N.insert(1,list_N.pop(-1))

    print(list_N)

def problem3_using_cuts():
    N = abs(int(input("Enter a number:")))

    list_N = []

    for i in range(-N,N+1):
        list_N.append(i)
    print(list_N)

    list_N = list_N[-2:] + list_N[:-2]

    print(list_N)


#Даны две строки. Подсчитайте сколько раз каждый символ первой строки 
# встречается во второй.
def problem4():
    phrase = input("Enter a phrase: ").lower
    sentence = input("Enter a sentence: ").lower

    count = 0
    for i in phrase:
        for j in sentence:
            if i == j:
                count+=1
        print(f'{i} - {count}')
        count = 0
    




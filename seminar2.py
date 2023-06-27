# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты 
# вверх одной и той же стороной. Выведите минимальное количество монет, 
# которые нужно перевернуть

def problem10():
    import random

    number_of_coins = int(input('Enter the number of coins: '))

    list_1 = [random.randint(0,1) for i in range(number_of_coins)]
    print(*list_1)
    count_r = 0
    count_g = 0
    for i in list_1:
        if i == 0:
            count_r +=1
        else: count_g +=1
    if count_r <= count_g:
        print(f'Нужно перевернуть {count_r} решки.')
    else: print(f'Нужно перевернуть {count_g} герба.')

# res = [random.randrange(1, 50, 1) for i in range(7)]

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y 
# (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

def problem12():
    import random
    num1, num2 = random.randint(1,1000), random.randint(1,1000)
    print(num1,num2)
    sum_of_numbers = num1 + num2
    product_of_numbers = num1 * num2
    print(f'The sum of numbers is {sum_of_numbers}')
    print(f'The product of numbers is {product_of_numbers}')

    potential_numbers_list = []
    for i in range(1,product_of_numbers+1):
        if product_of_numbers % i == 0:
            potential_numbers_list.append(i)
    print(*potential_numbers_list)

    for i in potential_numbers_list:
        for j in potential_numbers_list:
            if i + j == sum_of_numbers:
                print(f'The numbers Pete chose are {i} and {j}.')

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.

def problem14():
    base = 2
    power = 0
    max_num = int(input('Enter a number: '))
    while base**power <= max_num:
        print(f'{base}^{power} = {base**power}')
        power+=1




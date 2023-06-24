#Задача 2: Найдите сумму цифр трехзначного числа.
def problem2():
    number = int(input('Enter a 3-digit number: '))
    numbers_sum = 0

    while number != 0:
        numbers_sum += number %10
        number = number//10 
    print(numbers_sum)


""" Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, 
что Петя и Сережа сделали одинаковое количество журавликов, 
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе? """

def problem4():
    number = int(input('Enter the number of cranes created: '))
    Pete = number/6
    Sergey = number/6
    Katya = number - Pete - Sergey
    print(f'Katya made {Katya} cranes, Pete made {Pete} cranes, Sergey made {Sergey} cranes.')


""" Задача 6: Вы пользуетесь общественным транспортом? 
Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, 
где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
Вам требуется написать программу, которая проверяет счастливость билета. """

def problem6():
    number = int(input('Enter your 6-digit ticket number: '))
    i = 1
    first_numbers_sum = 0
    last_numbers_sum = 0

    while i <= 3:
        last_numbers_sum += number %10
        number = number//10
        i+=1

    i = 1

    while i <= 3:
        first_numbers_sum += number %10
        number = number//10
        i+=1

    if first_numbers_sum == last_numbers_sum:
        print("Yes! You got the lucky ticket! :)")
    else: print("No, you didn't get the lucky ticket :(")

""" Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек 
отломить k долек, если разрешается сделать один разлом по прямой между дольками 
(то есть разломить шоколадку на два прямоугольника). """
def problem8():
    chocolate_length = int(input("Please enter the chocolate length in number of squares: "))
    chocolate_width = int(input("Please enter the chocolate width in number of squares: "))
    break_number_of_squares = int(input("Please enter how many squares you want to break: "))

    if break_number_of_squares % chocolate_length == 0 or break_number_of_squares % chocolate_width  == 0:
        print("Yes, it is possible to break the squares off to from two squares. ")
    else: print("No, it's not possible to break the squares off to form two squares.")

problem8()
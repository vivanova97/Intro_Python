# #Is either number a square of the other?
# number1 = int(input('Enter the first number: '))
# number2 = int(input('Enter the second number:'))
# if (number1 == number2 * number2) | (number2 == number1 * number1):
#     print('Yes one number is a square of another.')
# else: print('No the numbers are not squares of each other.')

#Number entry until a zero is entered and add all numbers that can be divided by 3

# summ = 0
# number = None
# while number != 0:
#     number = int(input('Enter a number:'))
#     if number %3 == 0:
#         summ +=number
# print(summ)

# number = int(input('Enter a number: '))
# number = abs(number)
# negative_number = -number
# while negative_number <= number:
#     print(negative_number, end = ' ')
#     negative_number+=1

#Задача 2: Найдите сумму цифр трехзначного числа.
number = int(input('Enter a three-digit number: '))
numbers_sum = 0

while number != 0:
    numbers_sum += number %10
    number = number//10 
print(numbers_sum)

#Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
#Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, 
#что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
number = int(input('Enter the number of cranes created: '))
Pete = number/6
Sergey = number/6
Katya = number - Pete - Sergey
print(f'Katya made {Katya} cranes, Pete made {Pete} cranes, Sergey made {Sergey} cranes.')


# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
number = int(input('Enter a three-digit number: '))
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
    print("You've got the lucky ticket! :)")
else: print("Sorry! You didn't get the lucky ticket :(")




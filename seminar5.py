#Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
#и возводит число А в целую степень B с помощью рекурсии.

def power(A = 3,B = 3):
    if B != 0:
        return A * power(A,B-1)
    else:
        return 1


#Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух 
# целых неотрицательных чисел. Из всех арифметических операций допускаются 
# только +1 и -1. Также нельзя использовать циклы.
def summ(a,b):
    if b == 0:
        return a
    else:
        return 1 + summ(a,b-1)
    



        
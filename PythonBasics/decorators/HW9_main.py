"""Решить задания, которые не успели решить на семинаре.
Напишите следующие функции:
Нахождение корней квадратного уравнения
Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой 
чисел из csv файла.
Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса """

import csv, random
from HW9_decorators import write_result_to_json,calc_quadratic_eq_roots

# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.

@write_result_to_json
@calc_quadratic_eq_roots
def gen_csv_with_three_rand_nums(file_name, rand_num_range:tuple):
    
    """Takes in a tuple of two numbers, the lower and upper limit for random generation of 3
    numbers into a csv file with random number of lines(range by default 100 to 1000)"""

    with open(file_name, 'w', newline='') as csv_f:
        csv_writer = csv.DictWriter(csv_f, fieldnames=['num1', 'num2', 'num3'])
        csv_writer.writeheader()
        for _ in range(random.randint(100,1001)):
            num1, num2, num3 = [random.randint(*rand_num_range) for _ in range(3)]
            csv_writer.writerow({'num1':num1, 'num2': num2, 'num3':num3})

if __name__ == '__main__':
    gen_csv_with_three_rand_nums('rand_nums.csv',(1,20))

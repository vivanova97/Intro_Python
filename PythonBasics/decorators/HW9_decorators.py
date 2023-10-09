"""Decorators for HW9"""

import csv, json
from typing import Callable
from solve_quadratic_equation import solve_quadratic_equation

__all__ = ['write_result_to_json', 'calc_quadratic_eq_roots']

# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
def write_result_to_json(func: Callable):
    json_list = []
    
    def wrapper(*args, **kwargs):
        for row in func(*args, *kwargs):
            json_list.append(row)
        with open('quadratic_eq_input_output.json', 'a+', encoding='utf-8') as json_f:
            json.dump(json_list, json_f, ensure_ascii=False, indent=2)
    
    return wrapper    

# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой 
# чисел из csv файла.

def calc_quadratic_eq_roots(func: Callable):
    def wrapper(*args, **kwargs):
        func(*args)
        file_name, *_ = args
        with open(file_name, 'r+', newline='') as csv_f:
            reader_csv = csv.DictReader(csv_f)
            for line in reader_csv:
                num1 = int(line['num1'])
                num2 = int(line['num2'])
                num3 = int(line['num3'])
                yield {f'{num1},{num2},{num3}': str(solve_quadratic_equation(num1, num2, num3))}
                
    return wrapper
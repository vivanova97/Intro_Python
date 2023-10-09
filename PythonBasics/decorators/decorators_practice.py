# Decorator Practice: Logging Function Calls
# Create a decorator that logs when a function is called and what arguments it receives. 
# Apply this decorator to multiple functions and observe the logged information.
from typing import Callable
from functools import wraps
import time
import timeit

def logs(func: Callable):
    logs_dict = {}
    @wraps(func)
    def wrapper(*args):
        logs_dict['id'] = hash(f'{time.time()}'+f'{args}')
        logs_dict['id']= {'time':time.time(), 'args':args}
        print(logs_dict)
        return func(*args)
    return wrapper

@logs
def addition1(a,b):
    return sum((a,b))

# print(addition1(1,2))

# Decorator Practice: Execution Time Measurement
# Implement a decorator that measures and prints the execution time of a function. 
# Use it to time different functions and analyze their performance.

import timeit

def execution_time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()  # Get the start time
        result = func(*args, **kwargs)  # Call the original function
        end_time = timeit.default_timer()  # Get the end time
        execution_time = end_time - start_time  # Calculate execution time
        print(f"{func.__name__} took {execution_time} seconds to execute.")
        return result
    return wrapper

# Example usage of the decorator
@execution_time_decorator
def add(num):
    result = 0
    for i in range(num):
        result += i
    return result

@execution_time_decorator
def multiply(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

# Call the decorated functions
# add(1000)
# multiply(1000)

# Decorator Practice: Argument Validation
# Write a decorator that validates the arguments passed to a function based on specific 
# criteria (e.g., checking if all arguments are positive integers). Apply this decorator 
# to functions and handle invalid arguments gracefully.

def validate_int_args(func: Callable): 
    def wrapper(*args):
        try:
            if not all(list(map(lambda x: x == abs(int(x)), args))):
                raise ValueError('Not all arguments are positive integers.')
        except ValueError as e:
            print(f'Error: {e}')
        
        return func(*args)
    return wrapper

@validate_int_args
def add_nums(*args):
    return sum(args)

add_nums(1,2,3,4,5,6,7,8,9)

# 📌Создайте функцию-замыкание, которая запрашивает два целых числа: 
# ○ от 1 до 100 для загадывания, ○ от 1 до 10 для количества попыток 
# 📌Функция возвращает функцию, которая через консоль просит угадать загаданное 
# число за указанное число попыток.
import random

def guess():
    num = random.randint(1,100)
    num_of_guesses = random.randint(1,10)
    def guess_num():
        nonlocal num_of_guesses, num
        while num_of_guesses:
            guessed_num = int(input('Guess num: '))
            if num == guessed_num:
                print('You guessed correctly!')
                break
            elif num < guessed_num:
                print(f'Incorrect. The number is lower. {num_of_guesses} guesses left.')
                num_of_guesses-=1
            elif num > guessed_num:
                print(f'Incorrect. The number is higher. {num_of_guesses} guesses left.')
                num_of_guesses-=1
        else:   
                print(f'You ran out of guesses! The correct number is {num} ')
            
    return guess_num()

# 📌Напишите декоратор, который сохраняет в json файл параметры декорируемой функции 
# и результат, который она возвращает. При повторном вызове файл должен расширяться, 
# а не перезаписываться. 📌Каждый ключевой параметр сохраните как отдельный ключ json 
# словаря. 📌Для декорирования напишите функцию, которая может принимать как позиционные, 
# так и ключевые аргументы. 📌Имя файла должно совпадать с именем декорируемой функции.  
import json
import os
def json_decor(func:Callable):
    def wrapper(*args, **kwargs):
        result = func(*args,**kwargs)
        func_name = func.__name__

        if os.path.isfile(f'{func_name}.json') and os.path.exists(f'{func_name}.json'):
            with open(f'{func_name}.json', 'r+', encoding='utf-8') as json_f:
                dict_ = json.load(json_f)
        else:
            dict_ = {}
        # try:
        #     with open(f'{func_name}.json', 'r+', encoding='utf-8') as json_f:
        #             dict_ = json.load(json_f)

        # except FileNotFoundError:
        #         dict_ = {}
        print(dict_)
        if args:
                dict_[f'{result}'] = args
                
        if kwargs:
                dict_[f'{result}'] = kwargs
        
        with open(f'{func_name}.json', 'w', encoding='utf-8') as json_f:
            json.dump(dict_, json_f, ensure_ascii=False, indent=2)
    
    return wrapper

# 📌Объедините функции из прошлых задач. 
# 📌Функцию угадайку задекорируйте: ○ декораторами для сохранения параметров, 
# ○ декоратором контроля значений и ○ декоратором для многократного запуска. 
# 📌Выберите верный порядок декораторов.
def run_times(count:int):
    def decor(func:Callable):
        print(func)
        def wrapper(*args):
            for _ in range(count):
                func(*args)
        return wrapper
    return decor

# 📌Дорабатываем задачу 1. 📌Превратите внешнюю функцию в декоратор. 
# 📌Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] 
# и [1, 10]. 📌Если не входят, вызывать функцию со случайными числами из диапазонов.

def check_num_args(func: Callable):
    def wrapper(*args):
        try:
            a, b, *_ = args
            if a not in range(1,101):
                raise ValueError('First argument should be between 1-100. Random int selected.')
            elif b not in range(1,11):
                raise ValueError('Second argument should be between 1-10. Random int selected.')
        except ValueError as e:
            print(f'Error: {e}')
            a = random.randint(1,100)
            b = random.randint(1,10)
            return func(a,b)
        return func(*args)
    return wrapper

@json_decor
@run_times(3)
@check_num_args
def guess2(num, num_of_guesses):
    def guess_num2():
        nonlocal num_of_guesses, num
        while num_of_guesses:
            guessed_num = int(input('Guess num: '))
            if num == guessed_num:
                print('You guessed correctly!')
                return True
            elif num < guessed_num:
                num_of_guesses-=1
                print(f'Incorrect. The number is lower. {num_of_guesses} guesses left.')
            elif num > guessed_num:
                num_of_guesses-=1
                print(f'Incorrect. The number is higher. {num_of_guesses} guesses left.')
        else:   
                print(f'You ran out of guesses! The correct number is {num} ')
                return False
            
    return guess_num2()

guess2(100, 5)

@json_decor
def calculate_total(**kwargs):
    total = 0
    for product_name, value in kwargs.items():
        total += value
    return total

calculate_total(product1=125.0, product2=155.5, product3=77.25)

@json_decor
def add1(num):
    result = 0
    for i in range(num):
        result += i
    return result

add1(55)

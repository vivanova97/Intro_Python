'''
Homework for seminar2
'''

import math

def number_input() -> int:
    '''
    Gather numeric input from user
    '''
    while True:
        try:
            number = int(input('Please enter a number: '))
        except ValueError:
            print('That is not a number! Please enter a number:')
        else:
            break
    return number


def convert_number_to_hex() -> str:
    '''
    Using input provided by user, returns the hexidecimal form of the number.
    '''
    num = number_input()
    hex_dict = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:'a', 11: 'b', 12: 'c',\
                13:'d', 14: 'e', 15: 'f'}
    
    remainder_list = []

    while num > 0:
        remainder_list.append(num % 16)
        num = num//16

    hex_number = ''
    while remainder_list:
        hex_number += str(hex_dict[remainder_list.pop()])
    return hex_number


def fraction_input() -> tuple:
    '''
    Accept two fractions provided as strings "a/b" and returns the following tuple values:
    (first_fraction_numerator, first_fraction_denominator, second_fraction_numerator, 
    second_fraction_denominator)
    '''
    while True:
        try:
            first_fraction = input('Enter the first fraction: ').replace(' ', '')
            if not first_fraction[0].isdigit() or first_fraction[1] != '/' or not \
                first_fraction[2].isdigit():
                raise ValueError("Fraction should be written in this format: 'number/number'")
        except ValueError as e:
            print('Error', e)
        else:
            break

    first_fraction_numerator = int(first_fraction[0])
    first_fraction_denominator = int(first_fraction[2])

    while True:
        try:
            second_fraction = input('Enter the second fraction: ').replace(' ', '')
            if not second_fraction[0].isdigit() or second_fraction[1] != '/' or not \
                second_fraction[2].isdigit():
                raise ValueError("Fraction should be written in this format: 'number/number'")
        except ValueError as e:
            print('Error', e)
        else:
            break

    second_fraction_numerator = int(second_fraction[0])
    second_fraction_denominator = int(second_fraction[2])

    return (first_fraction_numerator, first_fraction_denominator, second_fraction_numerator, \
            second_fraction_denominator)


def sum_fractions():
    '''
    Sums two fractions provided as strings "a/b"
    '''
    first_fraction_numerator, first_fraction_denominator, second_fraction_numerator, \
        second_fraction_denominator = fraction_input()
    lcm = math.lcm(first_fraction_denominator, second_fraction_denominator)
    first_numerator_multiplier = int(lcm / first_fraction_denominator)
    second_numerator_multiplier = int(lcm / second_fraction_denominator)
    new_numerator = first_numerator_multiplier * first_fraction_numerator + \
        second_numerator_multiplier * second_fraction_numerator
    result = f'{new_numerator}/{lcm}'
    return result


def multiply_fractions():
    '''
    Multiplies two fractions provided as strings "a/b"
    '''
    first_fraction_numerator, first_fraction_denominator, second_fraction_numerator, \
        second_fraction_denominator = fraction_input()
    new_fraction_numerator = first_fraction_numerator * second_fraction_numerator
    new_fraction_denominator = first_fraction_denominator * second_fraction_denominator
    gcd = math.gcd(new_fraction_numerator, new_fraction_denominator)
    result = f'{int(new_fraction_numerator/gcd)}/{int(new_fraction_denominator/gcd)}'
    return result

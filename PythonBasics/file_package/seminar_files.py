import string
import random
import os
from pathlib import Path

__all__ = ['add_nums_to_file', 'name_gen', 'name_mult_nums', 'create_write_file',
           'gen_file_with_ext', 'sort_files']


_low_limit = -1000
_high_limit = 1000
def add_nums_to_file(file_name: str, num_of_lines: int):
    """
    Generates random number pairs in the following format: num | float.
    Appends the pairs to the file name provided in the function argument.
    The number of random pairs appended to the file depends on the num_of_lines argument provided.
    Low limit and high limit for random number generation are by default -1000, 1000 respectively.
    """

    with open(f'{file_name}', 'a+', encoding='utf-8') as f:
        for _ in range(num_of_lines):
            f.write(f'{random.randint(_low_limit,_high_limit)} | {random.uniform(_low_limit,_high_limit)}\n')


def name_gen(file_name: str):
    """
    The function generates random names from 4-7 characters in length
    and saves them to the file provided in the function arguments section.
    """

    name_character_len = random.randint(4,7)
    alphabet = string.ascii_lowercase
    rand_name = ''.join(random.sample(alphabet, name_character_len))
    if any(map(lambda letter: letter in ['a','e','i','o','u'], rand_name)):
        with open(f'{file_name}', 'a+', encoding='utf-8') as f:
            f.write(f'{rand_name.capitalize()}\n')
    else:
        name_gen()


def name_mult_nums(name_gen_file_name: str, numbers_file_name: str, new_combined_file: str):
    """
    Opens files created using add_nums_to_file and name_gen.  These file names need to be 
    included in the arguments section. 
    The number pairs are multipled. If the product from multiplicaton is negative, an absolute value
    is taken and the result is written in a new file along with the random name that was generated.
    If the product from multiplication is positive, the name and the product is added to the new file
    with the product being rounded to the nearest whole number.
    """

    with (
        open(f'{name_gen_file_name}', 'r', encoding='utf-8') as pass_file,
        open(f'{numbers_file_name}', 'r', encoding='utf-8') as num_file,
        open(f'{new_combined_file}', 'a+', encoding='utf-8') as new_file
    ):
        name_list = list(pass_file)
        name_index = 0
        name_list_len = len(name_list)
        for line in num_file:
            num_list = line.replace(' ', '').replace('\n', '').split('|')
            if (num:=int(num_list[0]) * float(num_list[1])) < 0:
                if name_index == name_list_len-1:
                    name_index = 0
                new_file.write(f'{name_list[name_index][:-1]} {abs(num)}\n')
                name_index +=1
            elif (num:=int(num_list[0]) * float(num_list[1])) >= 0:
                if name_index == name_list_len-1:
                    name_index = 0
                new_file.write(f'{name_list[name_index][:-1]} {round(num,0)}\n')
                name_index +=1


_min_name_len = 6
_max_name_len = 30
_min_random_byte_size = 256
_max_random_byte_size = 4096

def create_write_file(file_ext: str, num_of_files=42):
    """
    Creates file with randomly generated name between 30-256 characters in length.
    Writes random bytes into the file created.  The sum of bytes written in the file being 
    between 256-4096.  The number of files created is 42 by default but can be adjusted using
    the num_of_files argument.
    """
    alphabet = string.ascii_lowercase
    while num_of_files:
        rand_name_len = random.randint(_min_name_len, _max_name_len)
        rand_file_entry_byte_size = random.randint(_min_random_byte_size, _max_random_byte_size)
        rand_file_name = ''.join(random.choices(alphabet, k=rand_name_len))
        with open(f'{rand_file_name}.{file_ext}', 'wb+') as f:
            f.write(''.join(random.choices(alphabet, k=rand_file_entry_byte_size)).encode('utf-8'))
            num_of_files-=1

    
def gen_file_with_ext(num_of_files, *args):
    """
    Generates files with extensions provided in as strings in *args. The number of files 
    generated provided by user as an integer in the num_of_files argument. Extension is 
    randomly selected.
    """
    while num_of_files:
        create_write_file(random.choice(args), num_of_files=1)
        num_of_files-=1


def sort_files():
    """
    Sorts all files in current working directory and subfiles to folders txt and bin.
    """
    for root, dirs, files in os.walk(Path.cwd()):
        if ('txt_files' or 'bin_files') in root:
            continue
        for file in files:
            _, extension = os.path.splitext(file)
            if extension == '.txt':
                Path(file).replace(Path.cwd() / 'txt_files' / file)
            if extension == '.bin':
                Path(file).replace(Path.cwd() / 'bin_files' / file)

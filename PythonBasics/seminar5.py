'''
Homework for seminar 5
'''

'''One-line multiplication table generator from 2*2 to 9*10'''
mult_table_generator = ("\n" if i == 2 and j == 10 else f"{i} * {j} = {i*j} \t{i+1} * {j} = {(i+1) * j} \t{i+2} * {j} = {(i+2) * j} \t{i+3} * {j} = {(i+3) * j}" for i in range(2,7,4) for j in range (2,11))
# print(*mult_table_generator, sep = '\n')


def prime_number_generator(num_of_primes: int) -> int:
    '''
    Returns the number of prime numbers specified by user, starting at 2.
    '''
    num = 2
    while num_of_primes > 0:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            yield num
            num_of_primes -= 1

        num += 1


def macos_return_path_filename_extension(file_path: str) -> tuple :
    '''
    Returns the path, file_name, and extension in tuple format.
    '''
    *path, file_name_extension = file_path.split('/')
    path = '/'.join(path)
    file_name, extension = file_name_extension.split('.')
    
    return path, file_name, extension


'''The bonus_generator generates a dictionary of key, value pairs in the format -> {name:bonus_amount}'''
lst_name = ['Anna', 'Sergey', 'Elena']
lst_prem = ['10.25%', '10.75%', '11.50%']
lst_stv = [40000, 75000, 50000]

bonus_generator = ({lst_name[i]:lst_stv[i]*float(lst_prem[i][:-1])/100} for i in range(len(lst_name)))


def generate_fibonacci():
    '''Generates fibonacci sequence indefinitely until stopped by outside loop.'''
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fibon_generator_instance = generate_fibonacci()

for _ in range(20):
    print(next(fibon_generator_instance))

''' 
Important to remember:
When creating a generator that runs indefinitely,the generator must be stored 
in a variable. Calling on the generator inside a loop multiple times (like this: generator()) will
restart the generator from the beginning because a new instance is created.
By storing the generator in a variable outside the loop, you ensure that the generator retains 
its state between iterations, allowing it to continue producing the next values in the sequence.
'''


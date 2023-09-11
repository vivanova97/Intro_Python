'''
Homework for seminar 4.
'''

def transpose_matrix(matrix: list[list[int]] | list[tuple[int]]):
    '''Prints the transposed matrix.'''
    for item in zip(*matrix):
        print(*item)


def invert_dictionary_keys_values(**kwargs):
    '''
    Returns a dictionary where the arguments and keys are inverted.  If object-type of a value
    provided is changeable (as checked by hash function), it is formatted as a string before 
    becoming a key.
    '''
    new_dict = dict()
    for key, value in kwargs.items():
        try:
            hash(value)
        except TypeError:
            new_dict[str(value)] = key
        else:
            new_dict[value] = key
    return new_dict
 
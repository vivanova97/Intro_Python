"""
Homework for seminar 6, function to check if date exists.
"""
from sys import argv

__all__ = ['date_exists']

def date_exists(date: str) -> bool:
    """
    Checks if date exists, takes year in format DD.MM.YYYY and accepts years from 1 to 9999.
    """

    date = date.replace(' ', '').split('.')
    date = list(map(int, date))

    if 1 <= date[2] < 9999:
        if date[1] in [1,3,5,7,8,10,12]:
            if 1 <= date[0] <= 31:
                return True
        elif date[1] == 2:
            if 1 <= date[0] <= 28:
                return True
            elif date[0] == 29:
                return _leap_year_check(date[2])
        elif date[1] in [4,6,9,11]:
            if 1 <= date[0] <= 30:
                return True
    
    return False


def _leap_year_check(year:int):
    leap_year = False
    if year % 4 == 0:
        leap_year = True
    elif year % 100 == 0 and year % 400 == 0:
        leap_year = True
    return leap_year
        
        
if __name__ == '__main__':
    date = ''.join(argv[1:]) 
    print(date_exists(date))

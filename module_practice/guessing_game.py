"""
Practice Module
"""

from random import randint

__all__ = ['guess_game']

def guess_game(lower: int=0, upper: int=100, number_of_tries: int=5) -> bool:
    """
    Number-guessing game.
    """

    number = randint(lower, upper+1)
    
    while number_of_tries:
        guess = int(input('Enter your guess: '))
        if guess > upper or guess < lower:
            print(f"Number should be between {lower} and {upper}")
        elif guess == number:
            print('You guessed right!')
            return True
        elif guess > number:
            number_of_tries-=1
            print(f"The number is lower. Number of tries left: {number_of_tries}")
        elif guess < number:
            number_of_tries-=1
            print(f"The number is higher. Number of tries left: {number_of_tries}")
        if not number_of_tries:
            print(f'The number was {number}')
    
    return False
   

if __name__ == '__main__':
    print(guess_game())

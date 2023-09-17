"""
Использовалось во время семинара для guessing_game модуля
"""

from guessing_game import guess_game
from sys import argv

options = list(map(int, argv[1:]))
lower = 1
upper = 100
number_of_tries = 5

if len(options):
    if len(options) == 1:
        upper = options[0]
    elif len(options) == 2:
        lower, upper = options
    else:
        lower, upper, number_of_tries, *_ =  options

guess_game(lower, upper, number_of_tries)

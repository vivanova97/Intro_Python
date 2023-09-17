"""
Создайте модуль с функцией внутри. 
Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.
"""
from random import shuffle, choice

__all__ = ['trivia_game', 'print_statistics']

_statistics_number_ = dict()

def trivia_game_questions_generator():
    dict_of_possible_questions = {'How many legs on an octopus?': ['8', '10', '12', '6'], 'How many days in a year?': ['365', '265', '367'], \
                                   "Who was the first president of the United States?": ['George Washington', 'Abraham Lincoln', 'Henry Ford']}
    while dict_of_possible_questions:
        key = choice(list(dict_of_possible_questions))
        yield key, dict_of_possible_questions.pop(key)


def trivia_game(num_of_guesses: int):
    global _statistics_number_
    num_of_guesses_used = 0
    num_of_guesses_contstant = num_of_guesses
    for question, options in trivia_game_questions_generator():
        correct_answer_key = 1
        options = list(map(lambda item: item.lower(), options))
        dict_ = {num:item for num, item in enumerate(options, start=1)}
        shuffle(options)
        print(question, *options, sep='\n')
        while num_of_guesses:
            guess = input('Enter your guess: ').lower()
            if guess == dict_[correct_answer_key]:
                num_of_guesses_used+=1
                print('You guessed correctly!')
                break
            elif guess not in options:
                print("That's not one of the options, try again!")
            else:
                num_of_guesses_used+=1
                num_of_guesses-=1
                print(f'Incorrect guess.  Number of attempts left: {num_of_guesses} ')
        _statistics_number_[question] = num_of_guesses_used
        num_of_guesses_used = 0
        num_of_guesses = num_of_guesses_contstant


def print_statistics():
    global _statistics_number_
    for question, num_of_guesses in _statistics_number_.items():
        print(f'Question: {question} guessed in {num_of_guesses}')


if __name__ == '__main__':
    trivia_game(3)
    print_statistics()

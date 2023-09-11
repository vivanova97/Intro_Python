# hello = "Hello World!"

# print(hello[:5:-1])
# print("Hello \nWorld")

# x = 100/777
# print(x)

# print(x.__round__(3))

# list1 = 'one two three four five'
# list2 = 'six seven eight nine ten'

# list1 = list1.split()
# list2 = list2.split()

# list_final = list1 + list2
# print(list_final)
# list_final.insert(0,list_final[0].upper())
# print(list_final)

# list_final.insert(1,list_final[1].upper())



# list_final[4] = list_final[4].upper()

# print(list_final)
 
# hi = 'hello'
# hi = hi[::-1] #reverse string
# 'hello'[::-1]
# print(hi)

# j = ['h','a','c','b']
# j.sort()
# print(j)

# list3 = [1,2,[3,4,'hello']]
# list3[2][2] = 'goodbye'

# print(*list3)

# list4 = [5,3,4,6,1]
# list4.sort()
# print(list4)

# d = {'simple_key':'hello'}
# print(d['simple_key']) #grab 'hello'
# d = {'k1':{'k2':'hello'}}
# print(d['k1']['k2']) #grab 'hello'
# print(d['k1'].values()) #grab 'hello'
# d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
# print(*d['k1'][0]['nest_key'][1]) #grab 'hello'
# d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
# print(*d['k1'][2]['k2'][1]['tough'][2])

# j = (1,2,3,4)
# print(type(j))
# list5 = [1,2,2,33,4,4,11,22,3,3,2]
# list5 = set(list5)
# print(list5)

# l_one = [1,2,[3,4]]
# l_two = [1,2,{'k1':4}]

# # True or False?
# print(l_one[2][0] >= l_two[2]['k1'])


# Write a function that takes a dictionary as input and prints 
# both the keys and their corresponding values on separate lines.
def function_1(dictionary1):
    for key,value in dictionary1.items():
        print(key)
        print(value)

# Write a function that takes a list of strings as input and returns 
# a dictionary where the keys are the unique strings from the list, 
# and the values represent the number of occurrences of each string in the list.

def function2(list1):
    dictionary2 = dict()
    for item in list1:
        dictionary2[item] = list1.count(item)
    set(dictionary2)
    print(dictionary2)
# function2(['hi','hello', 'hi', 'hello', 'bye'])


# Given a dictionary with nested dictionaries, write a function 
# that calculates the sum of all values within the nested dictionaries.

def function3(dictionary3, summa = 0):
    for key, value in dictionary3.items():
        for value1 in value.values():
            summa = summa + value1
        print(f'{key} sum = {summa}')
        summa = 0
# function3({'key1': {'skey1':1,'skey2':2,'skey3':3}, 'key2': {'skey1':3,'skey2':4,'skey3':5}})
            

# Invert dictionary: Write a function that takes a dictionary as input and 
# returns a new dictionary where the keys and values are swapped.

def function4(dictionary4, newdict = dict()):
    newdict = dict()
    for key, value in dictionary4.items():
        newdict[value] = key
    print(newdict)
# function4({1:'a', 2: 'b', 3: 'c'})

# Find common keys: Write a function that takes two dictionaries as input 
# and returns a list of keys that are common in both dictionaries.

def function5(dict1, dict2, keys_in_common = []):
    keys_in_common = []
    for item1 in dict1:
        for item2 in dict2:
            if item1 == item2:
                keys_in_common.append(item1)
    print(*keys_in_common)

# function5({1:'a', 2: 'b', 3: 'c'}, {1:'a', 2: 'b', 5: 'c'})

# Dictionary comprehension: Given a list of strings, write a function that creates a dictionary 
# where the keys are the strings and the values are the lengths of the corresponding strings.

def function6(list6, dictionary6 = dict()):
    for item in list6:
        dictionary6[item] = len(item)
    print(dictionary6)
# function6(['hello', 'hi', 'bye'])

# Write a function that takes a dictionary as input and returns a new dictionary 
# where the keys are sorted in ascending order.
def function7(dictionary7, newdict = dict()):
    newdict = dict(sorted(dictionary7.items()))
    return newdict


# Problem 1: Odd Numbers Write a program that prints all odd numbers from 1 to 20. 
# Use a continue statement to skip even numbers.
# for num in range(21):
#     if num %2 == 0:
#         continue
#     print(num)
    


# Problem 2: Write a program that asks the user to enter a password. If the password contains at 
# least one uppercase letter, one lowercase letter, and one digit, print "Password accepted." 
# Otherwise, print "Password must contain at least one uppercase letter, one lowercase letter, and one digit." 
# Use break to exit the password validation loop once the criteria are met.

def solution_without_break():
    password = input('Enter a password:')
    uppercase = False
    lowercase = False
    integer2 = False

    for letter in password:
        if letter == letter.upper():
            uppercase = True
        if letter == letter.lower():
            lowercase = True
        if letter.isnumeric:
            integer2 = True
        if lowercase == True and uppercase == True and integer2 == True:
            print('Password accepted.')
            break
    else:
        print('Make sure to use one uppercase letter, one lowercase letter, and an integer in your password.')

# solution_without_break()
    
        
# Problem3: Write a program that generates a random number between 1 and 100. 
# Allow the user to guess the number. If the user's guess is correct, print "Congratulations!" 
# If the guess is too high, print "Too high, try again." If the guess is too low, print "Too low, try again." 
# Use a loop and the continue statement to allow the user to keep guessing until they get it right.
def guess_int():
    import random
    guessed_integer = int(input('Guess a number between 1-100: '))
    random_integer = random.randint(1,100)

    while guessed_integer != random_integer:
        if guessed_integer > random_integer:
            guessed_integer = int(input('Too high, try again: '))
            continue
        if guessed_integer < random_integer:
            guessed_integer = int(input('Too low, please try again: '))
    else: 
        print('You guessed it!')

# Problem 4: Menu Selection. Write a program that displays a menu with options: "1. Add", "2. Subtract", 
# "3. Multiply", "4. Divide", "5. Quit". Ask the user to enter their choice. Use a loop to keep displaying 
# the menu until the user selects "5. Quit". Use pass for the "Quit" option and implement the other calculations 
# using if statements.

# print('Pick an option from the menu: \n1. Add \n2. Subtract \n3. Multiply \n4. Divide \n5. Quit' )
# menu_option = int(input('Pick an option from the menu above: '))

# Given a sentence, count the number of words that have an odd number of letters. 
# Use the enumerate() function to iterate through the words and their indices.
def count_odd_words ():
    sentence = 'Hi, ow are you doing?'
    odd_length_word_count = 0
    for index, word in enumerate(sentence.split()):
        if len(word) %2 == 1:
            odd_length_word_count+=1
    print(odd_length_word_count)



# You have a list of student names and their corresponding scores. 
# Print the names of students who scored above 90 marks along with their scores. 
def students_and_scores():
    students_and_scores = [('Sergey', 100), ('Lera', 100), ('Lara', 95), ('Jacob', 50)]

    for name, score in students_and_scores:
        if score > 90:
            print(name,score)

# Given a list of integers, find the first index of a number that is divisible by 7. 
# Print both the index and the number. Use the enumerate() function to iterate through the list.
def print_index_number():
    list_of_numbers = [1, 3, 21, 44, 49]
    for index, number in enumerate(list_of_numbers):
        if number %7 == 0:
            print(f'index = {index} \nnumber = {number}')
            break


# You are working with a list of book titles and their publication years. 
# Create a dictionary where the keys are the publication years and 
# the values are lists of book titles published in that year. Use the enumerate() 
# function to iterate through the list of book titles and years.
def publication_dictionary():
    book_titles_years = [
        ('book1', 2000),
        ('book2', 2001),
        ('book3', 2002),
        ('book4', 2001),
        ('book5', 2004)
    ]
    publication_dict = dict()

    for title, year in book_titles_years:
        if year in publication_dict:
            publication_dict[year].append(title)
        else:
            publication_dict[year] = [title]
    print(publication_dict)



# Write a function that takes a list of words and returns the length of the longest 
# word along with its index. Use the enumerate() function to iterate through the list.
def solution1():
    list_of_words = ['bear', 'rabbit', 'dog', 'cat', 'crocodile', 'elephant']

    max_length = len(list_of_words[0])
    index_of_max_length_word = 0

    for index, word in enumerate(list_of_words):
        if max_length < len(word):
            max_length = len(word)
            index_of_max_length_word = index

    print(f'length: {max_length} \nindex: {index_of_max_length_word} \nword: {list_of_words[index_of_max_length_word]}')

def solution2():
    list_of_words = ['bear', 'rabbit', 'dog', 'cat', 'crocodile', 'elephant']

    max_length_word = max(list_of_words, key=len)

    print("Word with maximum length:", max_length_word)


# You have a list of tuples, where each tuple contains a person's name and their age. 
# Create a new list of people's names who are younger than 25. 
def name_age_practice_problem():
    name_age = [('Ivan', 23), ('Phillip', 20), ('Sergey', 31), ('Valeria', 25)]
    new_list = []

    for index, (name, age) in enumerate(name_age):
        if age < 25:
            new_list.append(name_age[index])

    print(new_list)

# Given a list of strings, find the index of the first string that starts with the letter 'a'. 
# Print both the index and the string. Use the enumerate() function to iterate through the list.
def first_letter_a():
    list_of_strings = ['hello', 'Hi', 'Anna', 'Look', 'Astra']
    index_of_word_with_a = 0
    found_word = False
    for index, word in enumerate(list_of_strings):
        for letter in word:
            if letter[0].lower() == 'a':
                index_of_word_with_a = index
                found_word = True
                break
        if found_word == True:
            break
    print(f'index: {index_of_word_with_a} \nword: {list_of_strings[index_of_word_with_a]}')


# Use for, .split(), and if to create a Statement that will print out words that start with 's':
def test1():
    st = 'Print only the words that start with s in this sentence'

    for word in st.split():
        if word[0].lower() == 's':
            print(word)

# Use range() to print all the even numbers from 0 to 10.
def test2():
    for number in range(11):
        if number %2 == 0:
            print(number)

# Use a List Comprehension to create a list of all numbers between 1 and 50 
# that are divisible by 3.
def test3():
    list_comprehension = [number for number in range(51) if number %3 ==0]
    print(list_comprehension)

# Go through the string below and if the length of a word is even print "even!"
def test4():
    st = 'Print every word in this sentence that has an even number of letters'

    for word in st.split():
        if len(word) %2 == 0:
            print(word)

# Write a program that prints the integers from 1 to 100. 
# But for multiples of three print "Fizz" instead of the number, 
# and for the multiples of five print "Buzz". For numbers which are multiples 
# of both three and five print "FizzBuzz".

def test5():
    for number in range(1,101):
        if number %3 == 0 and number %5 == 0:
            print('FizzBuzz')
        elif number %3 ==0:
            print('Fizz')
        elif number %5 ==0:
            print('Buzz')
        else:
            print(number)
    
    
# Use List Comprehension to create a list of the first letters of every word in the string below:
def test6():
    st = 'Create a list of the first letters of every word in this string'
    st_first_letter = [letter[0] for letter in st.split()]
    print(st_first_letter)

# Problem 1: Squares of Even Numbers 
# Create a list of the squares of even numbers from 1 to 10 using list comprehension.
def squares_of_even_numbers():
    squares_of_even_numbers = [number*number for number in range(1,11) if number %2 == 0]
    print(squares_of_even_numbers)

#Tuple practice problem to find employee of the month or person with most hours.
def employee_check(work_hours, current_max = 0, employee_of_month = ''):
    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
    return (employee_of_month, hours)
# work_hours = [('Abby', 100), ('Billy', 400), ('Cassie', 800)]

# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words 
# begin with same letter

def animal_crackers(text):
    wordlist = text.split()
    return print(wordlist[0][0] == wordlist[1][0])



# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or 
# if one of the integers is 20. If not, return False

def twenty_or_not(number1, number2):
    return print((number1 + number2) == 20 or number1 == 20 or number2 == 20)


def find_33(check_array):
    array_33 = [3,3]
    for index in range(len(check_array)-1):
        if [check_array[index], check_array[index+1]] == array_33:
            return True
    return False

    # PAPER DOLL: Given a string, return a string where for every character in the original 
    # there are three characters
    # paper_doll('Hello') --> 'HHHeeellllllooo'
    # paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

def paper_doll(string):
    new_string = ''
    for letter in string:
        new_string += letter*3
    return new_string

    # print(paper_doll('Hello'))

from random import randint
def black_jack():
    player1_numbers = [randint(1,11) for i in range(2)]
    player2_numbers = [randint(1,11) for i in range(2)]
    print(f'Player1 your cards are {player1_numbers}')
    print(f'Player2 your cards are {player2_numbers}')
    player1_total = sum(player1_numbers)
    player2_total = sum(player2_numbers)
    needcard1 = 'Y'
    needcard2 = 'Y'
    while player1_total < 21 and needcard1 == 'Y':
        needcard1 = input('Player1--Do you need another card? Put Y for yes and N for no:')
        if needcard1 == 'Y':
            player1_numbers.append(randint(1,11))
            print(f'Your cards are: {player1_numbers} ')
            player1_total = sum(player1_numbers)
    while player2_total < 21 and needcard2 == 'Y':
        needcard2 = input('Player2--Do you need another card? Put Y for yes and N for no:')
        if needcard2 == 'Y':
            player2_numbers.append(randint(1,11))
            print(f'Your cards are: {player2_numbers} ')
            player2_total = sum(player2_numbers)

    if sum(player1_numbers) == 21:
        print('Player1: Blackjack! Your cards: {player1_numbers}')
    elif sum(player1_numbers) <= 21:
        print(f'Player1: Your card total is {sum(player1_numbers)}')
    elif sum(player1_numbers) >= 21 and 11 in player1_numbers:
        if sum(player1_numbers) - 10 > 21:
            player1_total -= 10
            print('Player1: Bust! After deduction of 10 your total is still above 21: {player1_total}')
        else: 
            player1_total -= 10
            print(f'Player1, your total after deducting 10 is: {player1_total}')
    else:
        print(f'Player1: Bust! Cards: {player1_numbers} Total: {player1_total}')
    if sum(player2_numbers) == 21:
        print(f'Player2: Blackjack! Your cards: {player2_numbers}')
    elif sum(player2_numbers) <= 21:
        print(f'Player2: Your card total is {sum(player2_numbers)}')
    elif sum(player2_numbers) >= 21 and 11 in player2_numbers:
        if sum(player2_numbers) - 10 > 21:
            player2_total -= 10
            print('Player2: Bust! After deduction of 10 your total is still above 21: {player2_total}')
        else: 
            player2_total -= 10
            print(f'Player2, your total after deducting 10 is: {player2_total}')
    else:
        print(f'Player2: Bust! Cards: {player2_numbers} Total: {player2_total}')
    if player1_total <=21 and player2_total <= 21 and player1_total > player2_total:
        print('Player1 Wins!')
    elif player1_total <=21 and player2_total <= 21 and player1_total == player2_total:
        print('You tied!')
    elif player1_total <=21 and player2_total <= 21 and player2_total > player1_total:
        print('Player2 Wins!')
    elif player1_total >=21 and player2_total >= 21:
        print('You both got over 21! Both lose!')

    
# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers 
# starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). 
# Return 0 for no numbers.
# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14

# list1 = [6,5,1,1,1,9]
# summ = 0
# for index, number in enumerate(list1):
#     if index >= list1.index(6) and index <= list1.index(9):
#         continue
#     else: summ += list1[index]
# print(summ)

#  Write a function that takes a sentence as input and returns a list of individual words 
# in that sentence.

def string_to_list(string):
    return string.split()

# Given a list of words, write a function that returns a string where all the words are joined 
# by a hyphen ("-").

def list_to_string(list):
    return '-'.join(list)

# Write a program that takes a string containing multiple email addresses separated by semicolons. 
# Split the string and print each email address on a new line.

def print_emails(string):
    for email in string.split(';'):
        print(email)

# print_emails('email1@mail.ru;email2@email.ru;email3@email.ru')

# Create a program that prompts the user to input their age. 
# Use a flag to keep track of whether the user is underage (age less than 18) or not. 
# Print an appropriate message based on the flag value.

def age_check(age):
    is_over_18 = age >= 18
    if not is_over_18:
        print('Underage')
    else:
        print('Good')

# age_check(15)
    
# Write a function that checks if a given string is a palindrome 
# (reads the same forwards and backwards). 
# Use a flag to indicate whether the string is a palindrome or not.
def is_word_palindrome(word):
    word = word.lower()
    is_palindrome = word == word[::-1]
    if not is_palindrome:
        print('Not palindrome')
    else:
        print('Palindrome!')

# Create a program that simulates a basic user login system. 
# Ask the user to enter a username and password. Use a flag to keep track of whether 
# the user has successfully logged in or not. Print a message accordingly.

def password_check():
    username_entered = input('Username: ')
    password_entered = input('Password: ')
    correct_username = '8Klsk!' 
    correct_password = 'asdf2j' 
    login_successful = False
    if username_entered == correct_username and password_entered == correct_password:
        login_successful = True
    
    if login_successful:
        print('Welcome!')
    else:
        print('Wrong username or password.')
    
# Given a list of numbers, use filter and a lambda expression to filter out the even numbers.
# numbers_list = [1,2,3,4,5,6,7,8,9,10]
# even_numbers_list = list(filter(lambda number: number %2 == 0, numbers_list))

# Given a list of numbers, use map and a lambda expression to square each number.

# numbers_list = [1,2,3,4,5]
# squared_numbers_list = list(map(lambda number: number**2, numbers_list))

# Given a list of names, use filter and a lambda expression to filter out names 
# that have less than 4 characters.
# name_list = ['Sergey', 'Valeria', 'Ted', 'Molly', 'Bob', 'Sally']
# for name in filter(lambda name: len(name) < 4, name_list):
#     print(name)

# Given a list of strings, use map and a lambda expression to create a new list containing 
# the lengths of each string.
string_list = ['s', 'st', 'str', 'stri', 'strin', 'string']
string_length_list = [len(string) for string in string_list]


# Given a list of temperatures in Celsius, use map and a lambda expression to convert 
# them to Fahrenheit.
# celsius_temperatures = [0, 10, 20, 30, 40, 50]
# for fahrenheit_temp in map(lambda celsius_temp: (celsius_temp * 9/5) + 32, celsius_temperatures):
#     print(fahrenheit_temp)


# Given a list of words, use filter and a lambda expression to filter out the palindromes 
# (words that read the same forwards and backwards).
words = ['lol', 'door', 'cook', 'sos']
palindromes = list(filter(lambda word: word == word[::-1], words))

# Given a list of strings, use map and a lambda expression to convert each string to uppercase.
words2 = ['lol', 'door', 'cook', 'sos']
words2 = list(map(lambda word: word.upper(), words2))
words3 = [word.lower() for word in words2]

# Given a list of dictionaries representing people with their ages, 
# use filter and a lambda expression to filter out people who are under 30 years old.
# people_ages = {'Sergey': 31, 'Valeria': 25, 'Elena': 49}

# for person in filter(lambda person: person[1] < 30, people_ages.items()):
#     print(person)
    
# Given a list of student grades as percentages, use map and a lambda expression 
# to convert them to letter grades according to a certain scale.
# grades_as_percentages = {'Sergey': 100, 'Karen': 90, 'Sarah': 80}
# for person, adjusted_grade in map(lambda person: (person[0],person[1] * 0.01 * 50), grades_as_percentages.items()):
#     print(person, adjusted_grade)

# Given a dictionary of student names and their test scores, use filter and a 
# lambda expression to filter out students who scored less than 80.
# test_scores = [{'name': 'Sarah', 'score': 70},{'name': 'Sergey', 'score': 100}]

# for score in filter(lambda entry: entry['score'] < 80, test_scores):
#     print(score)

# Given a dictionary of student names and their test scores, use map and a lambda expression 
# to adjust the scores by adding 5 points to each score.

test_scores = [{'name': 'Sarah', 'score': 70},{'name': 'Sergey', 'score': 100}]
test_scores = list(map(lambda entry: entry['score'] + 5, test_scores))
# print(test_scores)


# Given a dictionary of people's names as keys and their ages as values, 
# use filter and a lambda expression to filter out people whose names have more than 6 characters.

# test_scores2 = [{'name': 'Savannah', 'score': 70},{'name': 'Sergey', 'score': 100}]
# for item in filter(lambda entry: len(entry['name']) > 6, test_scores2):
#     print(item)

# Given a dictionary of people's full names as keys, use map and a lambda expression 
# to create a new dictionary with the same keys but containing only the 
# first letter of each person's name.
test_scores3 = [{'name': 'Havannah', 'score': 70},{'name': 'Sergey', 'score': 100}]
test_scores4 = list(map(lambda entry: {'name': entry['name'][0], 'score': entry['score']}, test_scores3))
# print(test_scores4)

# Given a dictionary of people's names and their ages, use filter and a 
# lambda expression to filter out people whose ages are odd.
names_ages = [{'name': 'Sergey', 'age': 31}, {'name': 'Valeria', 'age': 25}, {'name': 'Nikita', 'age': 30}]

# for entry in filter(lambda entry: entry['age'] %2 == 1, names_ages):
#     print(entry)

# Given a dictionary of people's names and their ages, use map and a lambda expression 
# to create a new dictionary where age values are categorized as "young" for ages less than 30, 
# "middle-aged" for ages between 30 and 60, and "senior" for ages over 60.
names_ages = [{'name': 'Sergey', 'age': 31}, {'name': 'Valeria', 'age': 25}, {'name': 'Nikita', 'age': 30}, {'name': 'Betty', 'age': 85}, {'name': 'Ilma', 'age': 48}]

# Given a dictionary of student names and their grade levels 
# (e.g., 'Freshman', 'Sophomore', 'Junior', 'Senior'), use filter and a lambda expression 
# to filter out students who are not in their Junior or Senior years.
student_grades = {
    'Alice': 'Freshman',
    'Bob': 'Sophomore',
    'Charlie': 'Junior',
    'David': 'Senior'
}
# for student, grade_level in filter(lambda student: student[1] == 'Junior' or student[1] == 'Senior', student_grades.items()):
    # print (student, grade_level)

# Given a dictionary of student names and their test scores as lists, 
# use map and a lambda expression to calculate the average score for each student.
student_scores = {
    'Alice': [85, 92, 78],
    'Bob': [70, 80, 65],
    'Charlie': [95, 88, 92],
    'David': [60, 75, 82]
}

average_scores = dict(map(lambda student: (student[0], sum(student[1]) / len(student[1])), student_scores.items()))



# args and kwargs practice
# Write a function called sum_numbers that takes any number of arguments and returns
# the sum of all the provided numbers.
def sum_numbers(*args, total = 0):
    for number in args:
        total += number
    return total

# Write a function called build_url that takes a base URL and any number of keyword arguments 
# representing query parameters. The function should construct and return the complete URL with 
# query parameters.
def build_url(**kwargs):
    complete_url = 'https://address.com?'
    query_params = []
    for key, value in kwargs.items():
        query_params.append(f'{key}={value}')
    query_string = '&'.join(query_params)
    complete_url += query_string
    print(complete_url)
        
# build_url(param1 = 'klsdf', par1='hi')

# Find Maximum using *args
def find_max(*args):
    return max(args)

# print(find_max(1,2,3,410,30))

# Calculate Total Cost using **kwargs
cost_of_goods = {'eggs': 5, 'milk': 4, 'sugar': 2}

def total_cost(**kwargs):
    total_cost = 0
    for value in kwargs.values():
        total_cost +=value
    return total_cost

# print(total_cost(eggs = 5, milk = 4, sugar = 2))
        

# Write a function called calculate_total_cost that takes the base cost as a positional 
# argument and any number of additional keyword arguments representing optional extra costs. 
# The function should calculate and return the total cost.

def calculate_total_cost(base_cost, **extra_costs):
    total_cost = base_cost
    for cost in extra_costs.values():
        total_cost += cost
    return total_cost

# Example usage
base_cost = 100
extra_costs = {
    'shipping': 10,
    'taxes': 5,
    'insurance': 7
}


# Write a function called concatenate_strings that takes any number of string arguments 
# and returns their concatenation.
def concatenate_strings(*args):
    return ' '.join(args)

# print(concatenate_strings('hello', 'how', 'are', 'you'))


# Write a function called create_dictionary that takes any number of keyword arguments 
# and constructs a dictionary using those arguments.
# Each keyword argument's name becomes a key, and its value becomes the corresponding value
# in the dictionary.

def create_dictionary(**kwargs):
    new_dict = dict()
    for key, value in kwargs.items():
        new_dict[key] = value
    return new_dict

# print(create_dictionary(one = 'hello', two = 'goodbye'))

# Write a function called calculate_average that takes any number of numeric arguments and returns their average.

def calculate_average(*args):
    return sum(args)/len(args)

# print(calculate_average(3,5,7,8))

# Write a function called find_minimum that takes any number of arguments and 
# returns the minimum value among them.
def find_min(*args):
    return min(args)

# print(find_min(10,3,20,45))


# Write a function called create_html_element that takes an HTML tag name as 
# the first argument and any number of keyword arguments representing attributes. 
# The function should construct and return an HTML element string with the specified tag 
# and attributes.
def create_html_element(tag_name, **attributes):
    tag = '<' + tag_name
    for key, value in attributes.items():
        if value == 'text':
            continue
        tag += f"'{key}'=" + f"'{value}'"
    tag += '>'
    tag += f"'{attributes['text']}'" + f'</{tag_name}>'
    return tag
    
# print(create_html_element('a', href = 'link', text = 'text', title = 'title'))

# htmlTagName = 'a'
# arguments = {'href':'link', 'title':'title', 'text':'text'}

# "<a 'href'='link' 'title'='title'>'text'</a>"

# Write a function that computes the volume of a sphere given its radius.
def vol(rad):
    from math import pi
    return 4/3*(pi) * (rad**3)
# print(vol(3))


# Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num,low,high):
    return num >= low and num <= high
# print(ran_check2(5,2,10))
def ran_check2(num,low,high):
    if num >= low and num <= high:
        print(f'{num} is within {low} and {high}')
    else:
        print(f'{num} is NOT within {low} and {high}')
# ran_check2(2,2,10)


# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

# Expected Output : 
# No. of Upper case characters : 4
# No. of Lower case Characters : 33
# sample_string = 'Hello Mr. Rogers, how are you this fine Tuesday?'

def up_low(string_input):
    lower_count = 0
    upper_count = 0
    for letter in string_input:
        if letter.islower():
            lower_count+=1
        elif letter.isupper():
            upper_count+=1
    print(f'lowercase count: {lower_count} \nuppercase count: {upper_count}')
# up_low('Hello Mr. Rogers, how are you this fine Tuesday?')


# Write a Python function that takes a list and returns 
# a new list with unique elements of the first list.
def unique_list(lst):
    return list(set(lst))
# print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))



# Write a Python function to multiply all the numbers in a list.
# Sample List : [1, 2, 3, -4]
# Expected Output : -24
def multiply(numbers):  
    product = 1
    for number in numbers:
        product *= number
    return product
# print(multiply([1, 2, 3, -4]))


# Write a Python function that checks whether a word or phrase is palindrome or not.
phrase = 'nurses run'
word = 'kayak'

def palindrome(word_or_phrase):
    word_or_phrase = word_or_phrase.replace(' ', '')
    if word_or_phrase == word_or_phrase[::-1]:
        print('Palindrome!')
    else:
        print('Not palindrome!')
# palindrome(phrase)
# palindrome(word)


# Write a Python function to check whether a string is pangram or not. 
# (Assume the string passed in does not have any punctuation)

# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"

import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    str1 = list(set(str1.replace(' ', '').lower()))
    str1.sort()
    if str1 == list(alphabet):
        print('Pangram!')
    else:
        print('NOT Pangram!')
# ispangram("The quick brown fox jumps over the lazy dog")

def ispangram2(str1, alphabet=string.ascii_lowercase):
    str1 = set(str1.lower())
    missing_letters = set(alphabet) - str1
    if missing_letters:
        print('NOT Pangram!')
    else:
        print('Pangram!')
# ispangram2("The quick brown fox jumps over the lazy dog")


def display_list(game_list):
    print(f'Here is the current game list: {game_list}')

def position_choice(list_display):
    choice = 'Wrong'

    while not choice.isdigit() or choice not in range(len(list_display)):
        choice = input(f'Enter an index between 0 and {len(list_display)-1}: ')
        if not choice.isdigit():
            print("That's not an integer!")
        if choice.isdigit():
            if int(choice) not in range(len(list_display)):
                print(f'Choice not in range. Enter a number between 0 and {len(list_display)-1}: ')
            if int(choice) in range(len(list_display)):
                print(choice)
                return int(choice)
            
def replacement_choice(game_list, position):
    user_placement = input('Type a string to place at position: ')
    game_list[position] = user_placement
    return game_list


def gameon_choice():
    choice = 'Wrong'

    while choice not in ['Y', 'N']:
        choice = input('Keep playing? (Y or N)')
        if choice not in ['Y', 'N']:
            print("Sorry I don't understand, please choose Y or N.")
    if choice == 'Y':
        return True
    else: 
        return False
    
game_on = True
game_list = [0,1,2]

# while game_on:
#     display_list(game_list)
#     position = position_choice()
#     game_list = replacement_choice(game_list, position)
#     display_list(game_list)
#     game_on = gameon_choice()



def display_board(board_values):
    print(f'{board_values[0]}|{board_values[1]}|{board_values[2]}')
    print('_|_|_')
    print(f'{board_values[3]}|{board_values[4]}|{board_values[5]}')
    print('_|_|_')
    print(f'{board_values[6]}|{board_values[7]}|{board_values[8]}')

def player_assignment():
    marker = ' '
    while marker not in ['X', 'O']:
        marker = input("Player 1: Would you like to be X or O? Please type 'X' or 'O': ").upper()
        if marker not in ['X', 'O']:
            print("Incorrect response! Please type 'X' or 'O'")
    player1_marker = marker
    if player1_marker == 'X':
        player2_marker = 'O'
    else:
        player2_marker = 'X'
    return (player1_marker,player2_marker)

def game_play_p1(available_positions, board_values, player1):
    position = 'wrong'
    while not position.isdigit() or int(position) in available_positions:
        position = input('Player 1 choose a position you want to update: ') 
        if not position.isdigit():
            print("That's not a digit! Enter a digit 1-9 for the position which you want to update: ")
        elif int(position) in available_positions:
            print("Choose a position 1-9 that has not been chosen yet: ")
    available_positions.append(int(position))
    board_values[int(position)-1] = player1
    return (available_positions, board_values)

def game_play_p2(available_positions, board_values, player2):
    position = 'wrong'
    while not position.isdigit() or int(position) in available_positions:
        position = input('Player 2 choose a position you want to update: ') 
        if not position.isdigit():
            print("That's not a digit! Enter a digit 1-9 for the position which you want to update: ")
        elif int(position) in available_positions:
            print("Choose a position 1-9 that has not been chosen yet: ")
    available_positions.append(int(position))
    board_values[int(position)-1] = player2
    return (available_positions, board_values)

def check_win(board_values, player1, player2, available_positions):
    if board_values[0] == board_values[1] and board_values[1] == board_values[2]:
        if board_values[0] == player1:
            print('Player 1 wins!1')
            return True
        elif board_values[0] == player2:
            print('Player 2 wins!1')
            return True
    elif board_values[3] == board_values[4] and board_values[4] == board_values[5]:
        if board_values[3] == player1:
            print('Player 1 wins!2')
            return True
        elif board_values[3] == player2:
            print('Player 2 wins!2')
            return True
    elif board_values[6] == board_values[7] and board_values[7] == board_values[8]:
        if board_values[6] == player1:
            print('Player 1 wins!3')
            return True
        elif board_values[6] == player2:
            print('Player 2 wins!3')
            return True
    elif board_values[0] == board_values[3] and board_values[3] == board_values[6]:
        if board_values[0] == player1:
            print('Player 1 wins!4')
            return True
        elif board_values[0] == player2:
            print('Player 2 wins!4')    
            return True
    elif board_values[1] == board_values[4] and board_values[4] == board_values[7]:
        if board_values[1] == player1:
            print('Player 1 wins!5')
            return True
        elif board_values[1] == player2:
            print('Player 2 wins!5') 
            return True   
    elif board_values[2] == board_values[5] and board_values[5] == board_values[8]:
        if board_values[2] == player1:
            print('Player 1 wins!6')
            return True
        elif board_values[2] == player2:
            print('Player 2 wins!6')  
            return True 
    elif board_values[0] == board_values[4] and board_values[4] == board_values[8]:
        if board_values[0] == player1:
            print('Player 1 wins!7')
            return True
        elif board_values[0] == player2:
            print('Player 2 wins!7') 
            return True  
    elif board_values[2] == board_values[4] and board_values[4] == board_values[6]:
        if board_values[2] == player1:
            print('Player 1 wins!8')
            return True
        elif board_values[2] == player2:
            print('Player 2 wins!8') 
            return True
    elif len(available_positions) == 9:
        print("It's a tie!")
    return False

def play_again():
    play_again = 'X'
    while play_again not in ['Y', 'N']:
        play_again = input('Would you like to play again? Y or N: ').upper()
    if play_again == 'Y':
        return True
    else:
        return False


def tic_tac_toe():
    player1, player2 = player_assignment()
    board_values = [' ' for item in range(9)]
    available_positions = []
    win = False
    display_board(board_values)
    while len(available_positions) != 9 or not win:
        available_positions, board_values = game_play_p1(available_positions, board_values, player1)
        print('\n'* 100)
        display_board(board_values)
        win = check_win(board_values, player1, player2, available_positions)
        if win == True:
            break
        available_positions, board_values = game_play_p2(available_positions, board_values, player2)
        print('\n'* 100)
        display_board(board_values)
        win = check_win(board_values, player1, player2, available_positions)
    if play_again():
        tic_tac_toe()

# Classes and objects practice

# Bank Account Class:
# Create a BankAccount class with attributes for account number, account holder name, and balance. 
# Include methods for depositing, withdrawing, and checking the account balance.

class BankAccount():
    def __init__(self, account_number, account_holder_name, balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance
    def Deposit(self, deposit_amount):
        self.balance = self.balance + deposit_amount
    def Withdraw(self, withdraw_amount):
        self.balance = self.balance - withdraw_amount
    def CheckAccountBalance(self):
        print(f"Your balance: {self.balance}")

# my_account = BankAccount(12345, 'Valeria Ivanova', 50000.50)
# print(type(my_account))
# print(my_account.account_holder_name)
# print(my_account.account_number)
# print(my_account.balance)
# my_account.Deposit(1000)
# my_account.CheckAccountBalance()
# my_account.Withdraw(500)
# my_account.CheckAccountBalance()



# Rectangle Class:
# Create a Rectangle class with attributes for length and width. 
# Implement methods to calculate the area and perimeter of the rectangle.
class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def Area(self):
        return self.length * self.width
    def Perimeter(self):
        return (self.length * 2) + (self.width * 2)
    
# my_rectangle = Rectangle(10,15)
# print(my_rectangle.length)
# print(my_rectangle.width)
# print(my_rectangle.Area())
# print(my_rectangle.Perimeter())


# Student Class:
# Create a Student class with attributes for name, age, and a list of 
# courses they are enrolled in. Implement methods to add a course, drop a course, 
# and display the student's information.

class Student():
    def __init__(self, name, age, list_of_classes = []):
        self.name = name
        self.age = age
        self.list_of_classes = list_of_classes
    def AddCourse(self, course):
        self.list_of_classes.append(course)
        print(f"{course} added to {self.name}'s courses.")

# student_1 = Student(name = 'Anna', age = '14')
# student_1.AddCourse('language arts')
# print(student_1.list_of_classes)

# Car Class:
# Create a Car class with attributes for make, model, and year. 
# Include methods for starting the car, stopping the car, and displaying its details.
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.car_running = False
    def StartingCar(self):
        if not self.car_running:
            self.car_running = True
    def StoppingCar(self):
        if self.car_running:
            self.car_running = False
    def GetCarInfo(self):
        print(f'{self.make} \n{self.model} \n{self.year}')
        
# my_car = Car('Reno Sandero', 'X10', '2020')
# my_car.GetCarInfo()


# Book Class:
# Create a Book class with attributes for title, author, and publication year. 
# Implement methods to display book details and calculate the age of the book.
import datetime 
class Book():
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
    def BookDetails(self):
        print(f"Title: {self.title} \nAuthor: {self.author} \nYear: {self.publication_year} \nAge: {datetime.datetime.now().year - self.publication_year}")

# Book1 = Book("Crime and Punishment", "Dostoevsky", 1866)
# Book1.BookDetails()


# Employee Class:
# Create an Employee class with attributes for name, role, and salary. 
# Implement methods to give a salary raise and display employee information.

class Employee():
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary
    def SalaryRaise(self, increment):
        self.salary = self.salary + increment 
    def DisplayEmployeeInformation(self):
        print(f"{self.name} \n{self.role} \n{self.salary}")

# employee1 = Employee('Sarah', 'Accountant', 40000)
# print(employee1.salary)
# employee1.SalaryRaise(5000)
# print(employee1.salary)


# Library Catalog Class:
# Create a LibraryCatalog class that maintains a catalog of books. Include methods to add books, 
# remove books, and display the list of available books.

class LibraryCatalog():
    def __init__(self, books = []):
        self.books = books
    def AddBooks(self, book):
        self.books.append(book)
    def RemoveBooks(self, book):
        self.books.remove(book)
    def DisplayBooks(self):
        print(self.books)
# book_catalog = LibraryCatalog()
# book_catalog.AddBooks('Crime and Punishment')
# book_catalog.AddBooks('Miracle Morning')
# book_catalog.DisplayBooks()

# Temperature Converter Class:
# Create a TemperatureConverter class with methods to convert between Celsius and Fahrenheit 
# temperatures.

class TemperatureConverter():
    def CelsiusToFahrenheit(celsius):
        return (celsius * 9/5) + 32
    def FahrenheitToCelsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

# temperature = 75
# converted_temperature = TemperatureConverter.CelsiusToFahrenheit(temperature)
# print(converted_temperature)
        

# Fill in the Line class methods to accept coordinates as a pair of tuples and 
# return the slope and distance of the line.
from math import sqrt
class Line():
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    def slope(self):
        return (self.coor1[1] - self.coor2[1]) / (self.coor1[0] - self.coor2[0])
    def distance(self):
        return sqrt((self.coor1[0] - self.coor2[0]) + (self.coor1[1] - self.coor2[1]))
    def __str__(self):
        return f"point 1: {self.coor1} \npoint 2: {self.coor2}"
    def __len__(self):
        return self.distance()

# line1 = Line((5,30), (-20, 17))
# del line1
from math import pi
class Cylinder:
    pi = pi
    
    def __init__(self,height=1,radius=1):
        self.height = height 
        self.radius = radius
        
    def volume(self):
        return Cylinder.pi * self.radius**2 * self.height
    
    def surface_area(self):
        return (2 * Cylinder.pi * (self.radius ** 2) + (2 * Cylinder.pi * self.height) + Cylinder.pi * (self.radius**2))
            

# my_cylinder = Cylinder(2, 3)
# print(my_cylinder.volume())
# print(my_cylinder.surface_area())


# Bank Accounts:
# Create a base class BankAccount with attributes for account number and balance. 
# Implement methods for deposit and withdraw. Create subclasses SavingsAccount and 
# CheckingAccount that inherit from BankAccount and add specific behavior like calculating 
# interest for savings accounts and tracking overdrafts for checking accounts.

class BankAccount():
    def __init__(self, account_number, balance = 0):
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f'{amount} deposited')
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print('Insufficient funds.')

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        BankAccount.__init__(self, account_number, balance)
        self.interest_rate = interest_rate
    def accrue_interest(self):
        self.balance = self.interest_rate * self.balance
        return self.balance

# my_savings = SavingsAccount(1234, 5, 1.01)
# print(my_savings.balance)
# my_savings.deposit(5)
# print(my_savings.balance)
# print(my_savings.accrue_interest())

class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance=0, overdraft_limit=100):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f'{amount} withdrawn')
        else:
            print('Withdrawal exceeds overdraft limit.')



# Vehicles Hierarchy:
# Create a hierarchy of classes representing vehicles. Implement a base class Vehicle 
# with methods like start and stop. Then, create subclasses like Car, Motorcycle, and Truck 
# that inherit from Vehicle and add specific features like the number of wheels and seating 
# capacity.

class Vehicle():
    def __init__(self, vehicle_started = False):
        self.vehicle_started = vehicle_started
    def start(self):
        self.vehicle_started = True
    def stop(self):
        self.vehicle_started = False

class Car(Vehicle):
    number_of_wheels = 4
    def __init__(self, seating_capacity, vehicle_started=False):
        super().__init__(vehicle_started)
        self.seating_capacity = seating_capacity

class Motorcycle(Vehicle):
    number_of_wheels = 2
    def __init__(self, seating_capacity, vehicle_started=False):
        super().__init__(vehicle_started)
        self.seating_capacity = seating_capacity
    
# my_car = Car(5)
# print(my_car.number_of_wheels)
# print(my_car.seating_capacity)
# print(my_car.vehicle_started)


# Employees and Managers:
# Create a class Employee with attributes like name, salary, and role. Implement a method for 
# displaying employee details. Then, create a subclass Manager that inherits from Employee and 
# adds attributes like team size and responsibilities.

class Employee():
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role
    def employee_details(self):
        print(f'{self.name} \n{self.salary} \n{self.role}')

class Manager(Employee):
    def __init__(self, name, salary, role, team_size, responsibilities):
        super().__init__(name, salary, role)
        self.team_size = team_size
        self.responsibilities = responsibilities
    def __str__(self):
        return f"name: {self.name} \nsalary: {self.salary} \nrole: {self.role} \nteam size: {self.team_size} \nresponsibilities: {', '. join(self.responsibilities)}"

# manager1 = Manager('Jeff', 80000, 'Sales Manager', 20, ['supervising', 'organizing projects'])
# print(manager1)

# School System:
# Design a class Person with attributes for name and age. Create a subclass Student that inherits 
# from Person and adds attributes like grade level and courses. Then, create a subclass Teacher 
# that inherits from Person and adds attributes like subject and teaching experience.

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class Student(Person):
    def __init__(self, name, age, grade_level, courses = []):
        super().__init__(name, age)
        self.grade_level = grade_level
        self.courses = courses

class Teacher(Person):
    def __init__(self, name, age, subject, teaching_experience):
        super().__init__(name, age)
        self.subject = subject
        self.teaching_experience = teaching_experience

# student1 = Student('Anna', 14, 8, ['Geometry', 'Spanish', 'Orchestra'])
# print(student1.grade_level)
# print(*student1.courses)


# Online Store:
# Create a class Product with attributes like name, price, and category. Implement a method 
# to display product details. Then, create subclasses like Electronics, Clothing, and Books 
# that inherit from Product and provide specific details.

class Product():
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    def product_details(self):
        print(f'product name: {self.name} \nproduct price: {self.price} \nproduct category: {self.category}')
        
class Electronics(Product):
    def __init__(self, name, price, category, genre, title, author, year):
        super().__init__(name, price, category)
        self.genre = genre
        self.title = title
        self.author = author
        self.year = year

# Errors and Exceptions Homework
# Handle the exception thrown by the code below by using try and except blocks.  
# try:
#     for i in ['a','b','c']:
#         print(i**2)
# except TypeError:
#     print('Type error!')
# else:
#     print('Correct input.')

# Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'

x = 5
y = 1

# try:    
#     z = x/y
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# else:
#     print(x/y)
#     print("Done!")

# Write a function that asks for an integer and prints the square of it. 
# Use a while loop with a try, except, else block to account for incorrect inputs.
def data_validation_practice():
    while True:
        try:
            number = int(input('Enter a number: '))
            print(number**2)
            break
        except: 
            print("Not a number! Enter a number:")
            continue

# Phone Number Validation:
# Write a program that validates a user's phone number input. The phone number 
# should have exactly 10 digits and should consist of only digits.
# while True:
#     try:
#         phone_number = input("Enter a phone number: ")
#     except:
#         print('Error! Phone number should contain integers only.')
#         continue
#     else:
#         if len(phone_number) != 10:
#             print('Invalid phone number. Phone number should be 10 digits.')
#             continue
#         else:
#             break


# Email Address Validation:
# Create a program that validates an email address entered by the user. 
# Ensure that the email address contains the "@" symbol and a valid domain name.

def EmailAddressValidation():
    valid_domains = ['gmail.com', 'hotmail.com', 'mail.ru', 'yahoo.com']
    while True:
        try:
            email_address = input("Enter your email address: ")
            if '@' not in email_address:
                raise ValueError('needs @')
            if email_address[email_address.index('@')+1:].lower() not in valid_domains:
                raise ValueError('need valid domain')
        except ValueError as e:
            print('Error', e)
            continue
        else:
            break
        

# Password Strength Checker:
# Write a program that checks the strength of a user's password. 
# The password should have a minimum length of 8 characters and should contain 
# a mix of uppercase and lowercase letters, numbers, and special characters.

class InvalidInputError(Exception):
    def __init__(self, message):
        self.message = message

def password_check():
    while True:
        try:
            password = input('Enter a password containing at least 8 characters and a mix of uppercase and lowercase letters, numbers, and special characters: ')
            if len(password) < 8:
                raise InvalidInputError('less than 8 characters')
            if not any(letter.islower() for letter in password):
                raise InvalidInputError('no lowercase letters')
            if not any(letter.isupper() for letter in password): 
                raise InvalidInputError('no uppercase letters')
            if not any(letter in '!@#$%^&*(),.?\":}|{<>' for letter in password):
                raise InvalidInputError
        except InvalidInputError as e:
            print('Error:', e)
        else:
            print('Password is all set!')
            break
    

# Numeric Input Validation:
# Develop a program that asks the user to input a numeric value. Handle cases where 
# the input cannot be converted to a number.
def number_check():
    while True:
        try:
            number = int(input('Enter a number: '))
        except ValueError:
            print('That is not an number!  Please enter a number:')
        else:
            break

# Username Availability:
# Create a program that prompts the user to enter a username. Check if the username is available 
# (not already taken). Use a dictionary to keep track of usernames.
def CheckIfUsernameExists():
    usernames = {}

    usernames['john_dow'] = {'name': 'John Doe', 'email': 'johnexample.com'}
    usernames['sarah_jane'] = {'name': 'Sarah Jane', 'email': 'sarahexample.com'}

    print(usernames)
    while True:
        try:
            username = input('Enter a username: ')
            if username in usernames.keys():
                raise ValueError('Username is taken. Try another.')
        except ValueError as e:
            print('Error:', e)
        else:
            break

# File Existence Checker:
# Write a program that asks the user for a filename and checks if the file exists. 
# Handle cases where the file doesn't exist.



# Date Validation:
# Develop a program that validates a date entered by the user in the format "YYYY-MM-DD". 
# Ensure that the year, month, and day are within valid ranges.

# Positive Integer Input:
# Create a program that prompts the user for a positive integer input. Handle cases where 
# the input is not a positive integer.

# Menu Input Validation:
# Write a program that displays a menu and asks the user to select an option. 
# Validate the user's choice to ensure it's within the valid range of options.

# Credit Card Number Validation:
# Develop a program that validates a credit card number entered by the user. 
# Check if the card number follows the Luhn algorithm.


# my_list = [1,2,3,4]
# print(id(my_list))
# my_list.append(5)
# print(my_list)
# print(id(my_list))
# print(hash(my_list))

# a = 2
# print(id(a))
# a = 5
# print(id(a))
# b = 5
# print(id(b))

# word = input('Enter something: ').split(',')
# word: int = int(input('Enter something: '))
# print(f'type: {type(word)} \naddress: {id(word)}')
# print(word)
# print(dir(str))
# a = 'Hello'
# print(id(a))
# a = 'Bye'
# print(id(a))
# b = 'Hello'
# print(id(b))
# help()
def using_enumerate():
    animals = ['dog', 'cat', 'elephant']
    for i, animal in enumerate(animals, start = 1):
        print(i, animal)

def number_to_hex():
    while True:
        try:
            num = int(input('Please enter a number: '))
        except ValueError:
            print('That is not a number! Please enter a number:')
        else:
            break

    hex_dict = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:'a', 11: 'b', 12: 'c',\
                13:'d', 14: 'e', 15: 'f'}
    remainder_list = []
    while num > 0:
        remainder_list.append(num % 16)
        num = num//16
        print(num)
        print(remainder_list)

    hex_number = ''
    while remainder_list:
        hex_number += str(hex_dict[remainder_list.pop()])
    print(hex_number)


def duplicate_elements(user_list):
    return set(filter(lambda item: user_list.count(item) > 1, user_list))


def ten_most_common_words():
    '''
    Returns 10 most common words in the text provided 
    '''
    article = input('Enter text: ').lower()

    non_alphabet = '''( ) ` ~ ! @ # $ % ^ & * - + = | \ { } [ ] : ; " ' < > , . ? / _1234567890'''

    for nonchar in non_alphabet:
        article = article.replace(nonchar, ' ')

    article_list = article.split()

    word_count_dict = dict()

    for word in article_list:
        word_count_dict[word] = article_list.count(word)

    sorted_word_count_dict = dict(sorted(word_count_dict.items(), key=lambda item: item[1]))

    ten_most_common_words = []
    
    for _ in range(10):
        ten_most_common_words.append(sorted_word_count_dict.popitem())
        
    print(ten_most_common_words)


# things_dict = {'pen': 10, 'book': 500, 'notebook': 1500, 'refrigerator': 30000, 'lunch': 500, \
#                'chair': 10000, 'coat': 900, 'wallet': 150, 'umbrella': 300, 'medicine': 100, \
#                 'random_item': 3000}

# backpack_capacity = 3000

def backpack_variations(things_dict, backpack_capacity):
    backpack = 0

    all_possible_variations = []
    things_dict = dict(filter(lambda item: item[1] < backpack_capacity, things_dict.items()))

    for key1, value1 in things_dict.items():
        backpack = value1
        possible_variation = [key1]  # Create a new list for each variation
        for key2, value2 in things_dict.items():
            if backpack < backpack_capacity and key2 not in possible_variation:
                backpack += value2
                possible_variation.append(key2)
        all_possible_variations.append(possible_variation)
        backpack = 0

    for list_item in all_possible_variations:
        list_item.sort()

    i = 1
    for list_item_i in all_possible_variations[i]:
        for list_item_j in all_possible_variations[i-1]:
            if list_item_i == list_item_j:
                all_possible_variations.pop(i)

    for variation in all_possible_variations:
        print(variation)

# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

# tuple_values = (1, 'hi', 2, 'bye', (1,2,3), [1,23,4], 5)
# my_dict = dict()
# for item in tuple_values:
#     if type(item) not in my_dict:
#         my_dict[type(item)] = []
#     my_dict[type(item)].append(item)
# print(my_dict)

# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.
def delete_elements_that_appear_twice():
    from pprint import pp
    list_ = [1,1,2,3,4,5,5,6,7,7,7]
    pp(list(filter(lambda list_item: list_.count(list_item) !=2, list_)))
    for index, item in enumerate(list_):
        if list_.count(item) == 2:
            list_.remove(item)
            list_.remove(item)
    pp(list_)

# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки.
def practice_problem():
    text = input('Enter text: ')
    list_ = text.split()
    list_.sort()
    max_word = max(list(map(lambda list_item: len(list_item), list_)))
    print(max_word)
    for index, word in enumerate(list_, start= 1):
        print(f'{index} {word:>{max_word}}')

#  Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается
# каждая буква в строке без использования
# метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ —
# символ, а значение — частота встречи
# символа в строке.
# ✔ Обратите внимание на порядок ключей.
# Объясните почему они совпадают
# или не совпадают в ваших решениях.
def letter_count_dict():
    text = 'hello how are you doing today'
    letter_count = dict()
    for letter in text:
        letter_count[letter] = text.count(letter)
    print(letter_count)

# ✔ Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

friends_things = {'Sergey': ('thermos', 'chair', 'umbrella'), 'Valeria': ('thermos', 'food'), 'Phill': ('table', 'thermos', 'table')}
set_list = []
i = 0
while i <= len(friends_things):
    for key, value in friends_things.items():
        set_list.append(set(value))
        i+=1
        
for index, set_item in enumerate(set_list, start=1):
    common_among_all = set_list[0].intersection(set_item)
    only_one_friend_has = set_list[0].difference(set_item)


# ✔Напишите функцию, которая принимает строку текста. 
# Вывести функцией каждое слово с новой строки. 
# ✔Строки нумеруются начиная с единицы. 
# ✔Слова выводятся отсортированными согласно кодировки Unicode. 
# ✔Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между 
# ним и номером строки.

def print_string_on_newline(string_input: str):
    string_list = string_input.lower().split()
    string_list.sort()
    max_length = len(max(string_list, key=len))
    for index, word in enumerate(string_list,start = 1):
        print(f'{index}. {word:>{max_length}}')


# ✔Напишите функцию, которая принимает строку текста. 
# ✔Сформируйте список с уникальными кодами Unicode каждого символа введённой строки 
# отсортированный по убыванию.

def string_to_unicode(string_input: str):
    unicode_list = []
    for symbol in set(string_input):
        unicode_list.append((ord(symbol)))
    unicode_list.sort(reverse=True)
    return unicode_list

def string_to_unicode2(string_input: str):
    return [ord(symbol) for symbol in sorted(set(string_input),reverse=True)]

# print(string_to_unicode2('How are you?'))

# ✔Функция получает на вход строку из двух чисел через пробел. 
# ✔Сформируйте словарь, где ключом будет символ из Unicode, а значением — целое число. 
# ✔Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего 
# включительно.
# string_input2 = input('Enter two numbers, separate the numbers with a space: ')

def unicode_dict(string_input: str) -> dict:
    start, finish = tuple(string_input.split())
    number_list = [item for item in range(int(start), int(finish)+1)]
    unicode_number_dict = sorted({chr(value): value for value in number_list}.items(), key= lambda item: item[1])
    print(unicode_number_dict)

# unicode_dict(string_input2)

# ✔Функция принимает на вход три списка одинаковой длины: ✔ имена str, ✔ ставка int, ✔ премия str 
# с указанием процентов вида «10.25%». 
# ✔Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения. 
# ✔Сумма рассчитывается как ставка умноженная на процент премии.

name_list = ['Sergey', 'Valeria', 'Elena']
percent_list = [.1125, .1217, .1245]
bonus_list = [170000, 150000, 140000]

def name_bonus(name_list: list[str], percent_list:[float], bonus_list:[float]) -> dict:
    name_amount = dict()
    for name, percent, bonus in zip(name_list,percent_list,bonus_list):
        name_amount[name] = "{:.2f}".format(percent * bonus)
    return name_amount

# print(name_bonus(name_list, percent_list, bonus_list))

# ✔Функция получает на вход список чисел и два индекса. 
# ✔Вернуть сумму чисел между между переданными индексами. 
# ✔Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.

def sum_of_numbers(numbers_list, index1, index2):
    if index1 < 0:
        index1 = 0
    if index2 > len(numbers_list)-1:
        index2 = len(numbers_list)-1
    return sum(numbers_list[index1:index2])-numbers_list[index1]

# numbers_list = [10,20,30,40,50,60,70,80,90,100,110,120]
# print(sum_of_numbers(numbers_list, 2,13))

# ✔Функция получает на вход словарь с названием компании в качестве ключа и списком с 
# доходами и расходами (3-10 чисел) в качестве значения. 
# ✔Вычислите итоговую прибыль или убыток каждой компании. 
# Если все компании прибыльные, верните истину, а если хотя бы одна убыточная — ложь.
company_list = {'H&M': [-100,2000,-200], 'Apple': [100000, -1001000, -500], 'Mavi': [15000, -5000]}
def check_all_companies_made_income(company_income_expenses: dict[str:list]):
    companies_income = list(map(lambda income_list: sum(income_list), company_income_expenses.values()))
    return all(map(lambda income: income > 0, companies_income))

# print(check_all_companies_made_income(company_list))

# ✔Создайте несколько переменных заканчивающихся и не оканчивающихся на «s». 
# ✔Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s 
# (кроме переменной из одной буквы s) на None. ✔Значения не удаляются, а помещаются в 
# одноимённые переменные без s на конце.

def variables_func():
    apples = 7
    s = 8
    sun = 10
    chairs = 15
    def change_value_of_words_ending_in_s():
        for key in locals():
            if key.endswith('s') and len(key) > 1:
                locals()[key] = None
    change_value_of_words_ending_in_s()
    print(locals())


# Напишите функцию для транспонирования матрицы
matrix = [[1,2,3], [4,5,6], [7,8,9]]
def transpose_matrix(matrix: list[list|tuple]):
    for item in zip(*matrix):
        print(*item)
# transpose_matrix(matrix)

# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
# где ключ — значение переданного аргумента, а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.
def invert_dictionary_keys_values(**kwargs):
    new_dict = dict()
    for key, value in kwargs.items():
        try:
            hash(value)
        except TypeError:
            new_dict[str(value)] = key
        else:
            new_dict[value] = key
    return new_dict

print(invert_dictionary_keys_values(hi=2, hello=[1,2,3,4], li=(2,3,4), dict_={'dog': 4, 'cat':2}))

    













    
    






    
    


        



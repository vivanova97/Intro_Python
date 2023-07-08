# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко 
# он их придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (
# т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, 
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, 
# если с ритмом все не в порядке

def check_for_vowels(phrase, count = 0):
    vowels = ['а', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и', 'ы']
    for letter in phrase:
        if letter.lower() in vowels:
            count+=1
    return count

def check_if_poem():
    poem = input("Enter a poem: ").split()
    vowels_count = list(map(check_for_vowels, poem))
    vowels_count = set(vowels_count)
    print('Парам пам-пам') if len(vowels_count) == 1 else print('Пам парам')
        
# check_if_poem()

# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки
# и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, 
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы 
# (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, 
# у которой ровно два аргумента, как, например, у операции умножения.

def multiply(row_num, column_num):
    return row_num * column_num

def print_operation_table(multiply, num_columns, num_rows):
        table = [[multiply(i+1,j+1) for i in range(num_columns)] for j in range(num_rows)]
        for row in table:
             print(*row)
        
# print_operation_table(multiply,6,6)

    

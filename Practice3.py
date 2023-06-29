def sum_number(n, summ = 0):
    for i in range(1,n+1):
        summ += i
    return summ

    a = sumNumber(5)
    print(a)

def scrabble_problem(word):
      
    dictionary = {'А':1, 'В':1, 'Е':1, 'И':1, 'Н':1, 'О':1, 'Р':1, 'С':1, 'Т':1, 'Д':2, 'К':2, 'Л':2, 'М':2, 'П':2, 'У':2, 'Б':3, 'Г':3, 'Ё':3, 'Ь':3, 'Я':3, 'Ж':5, 'З':5, 'Х':5, 'Ц':5, 'Ч':5, 'Ш':8, 'Э':8, 'Ю':8, 'Ф':10, 'Щ':10, 'Ъ':10, 'A':1, 'E':1, 'I':1, 'O':1, 'U':1, 'L':1, 'N':1, 'S':1, 'T':1, 'R':1, 'D':2, 'G':2, 'B':3, 'C':3, 'M':3, 'P':3, 'F':4, 'H':4, 'V':4, 'W':4, 'Y':4, 'K':5, 'J':8, 'X':8, 'Q':10, 'Z':10}

    summa = 0
    for i in word.upper():
            summa += dictionary[i]
    print(summa)


def quick_sort (list):
     length = len(list)
     if length <= 1:
          return list
     else: 
          pivot = list.pop()
     greater_than_pivot = []
     less_than_pivot = []
     for item in list:
        if item > pivot:
            greater_than_pivot.append(item)
        else:
            less_than_pivot.append(item)
     return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)




list = [1,2,3,4,5]
pivot = list.pop()
pivot = [pivot]
print(type(pivot))
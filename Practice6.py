from random import randint

list1 = [randint(1,100) for i in range(10)] #creates list of 10 random numbers in list
print(list1)
list1 = list(filter(lambda i: i % 2 == 0, list1)) #random numbers are limited in the list to only even numbers
print(list1)
list2 = [(x,x**2) for x in list1] #creating a second list that displays the number and its square

print(list2)





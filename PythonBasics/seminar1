def multiplication_table():
    #Prints multiplication table from 2*2 to 9*10
    for i in range(2,7,4):
        for j in range(2,11):
            print(f"{i} * {j} = {i*j} \t{i+1} * {j} = {(i+1) * j} \t{i+2} * {j} = {(i+2) * j} \t{i+3} * {j} = {(i+3) * j}")
            if i == 2 and j == 10:
                print()

def is_triangle(side1, side2, side3):
    #Checks if sides given form a triangle
    is_triangle = False
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        is_triangle = True

    if is_triangle:
        if side1 == side2 == side3:
            print(f"equilateral triangle")
            return
        elif side1 != side2 != side3:
            print(f"scalene triangle")
            return
        elif side1 == side2 or side1 == side3 or side2 ==side3:
            print(f"isosceles triangle")
            return
    print("The lines provided do not form a triangle.")

def is_prime():
    #Checks if number is prime
    number = 'not a number'
    while not number.isdigit() or int(number) > 100000 or int(number) < 0:
        number = input("Input any number from 2 to 100,000: ")
    number = int(number)
    
    is_prime = True
    if number < 2 or number %2 == 0:
        is_prime = False
    else: 
        for i in range(3,number-1,2):
            if number %i == 0:
                is_prime = False
                break

    if is_prime:
        print(f'{number} is prime!')
    else:
        print(f'{number} is not prime!')

                
            
        
            

    
import math

__all__ = ['solve_quadratic_equation']

# Нахождение корней квадратного уравнения
def solve_quadratic_equation(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    # Check the value of the discriminant
    if discriminant > 0:
        # Two distinct real roots
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        # One real root (root of multiplicity 2)
        root = -b / (2*a)
        return root
    else:
        # Complex roots
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2
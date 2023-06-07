# Quadratic equation: ax^2 + bx + c = 0
# Formula to find the roots: (-b + sqrt(b^2 - 4ac)) / 2a and (-b - sqrt(b^2 - 4ac)) / 2a

import math

a = float(input("Enter the coefficient of x^2: "))
b = float(input("Enter the coefficient of x: "))
c = float(input("Enter the constant term: "))

# Calculate the discriminant
discriminant = b**2 - 4*a*c

# Check if the discriminant is positive, negative or zero
if discriminant > 0:
    # Two real roots
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("The roots are:", root1, "and", root2)
elif discriminant == 0:
    # One real root
    root = -b / (2*a)
    print("The root is:", root)
else:
    # Two complex roots
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-discriminant) / (2*a)
    print("The roots are:", real_part, "+", imaginary_part, "i and", real_part, "-", imaginary_part, "i")

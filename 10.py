#Quadratic calculator

import math

#Input coefficients
a = float(input("What is coefficient a: "))
b = float(input("What is coefficient b: "))
c = float(input("What is coefficient b: "))

#Calculate discriminant
discriminant = b**2 - 4*a*c

#Check if discriminant is positive or negative
if discriminant > 0:
    #Two real distinct roots
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Root 1: {root1}, Root 2: {root2}")

elif discriminant == 0:
    #One real root, repeated
    root = -b / (2*a)
    print(f"Root: {root}")

else:
    #Complex imaginary roots
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
    print(f"Root 1: {real_part} + {imaginary_part}i; Root 2: {real_part} - {imaginary_part}i")

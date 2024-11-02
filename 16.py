#Program to find all the rpime numbers within an interval
import math
lower = int(input("Lower bound: "))
upper = int(input("Upper bound: "))

print(f"Prime numbers between {lower} and {upper} are: ")

for num in range(lower, upper + 1):
    #all primes are greater than 1
    if num > 1:
        for i in range(2, int(math.sqrt(num)) + 1):
            if (num % i) == 0:
                break
        else:
            print(num, end=" ")
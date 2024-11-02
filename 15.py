#Program that checks prime numbers
import math
num = int(input("Enter a number: "))

#Define a flag variable
flag = False

if num == 1:
    print(f"{num} is not a prime number.")
elif num > 1:
    #Check for factors
    #Instead of iterating through all the values, we can just iterate through values <√num
    for i in range(2, int(math.sqrt(num)) + 1):
        if (num % i) == 0:
            flag = True #if factor is found set flag to true
            #break of loop
            break
#Check flag status
if flag:
    print(f"{num}, is not a prime number")
else:
    print(f"{num}, is a prime number")
        

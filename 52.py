#Find the smallest number in a list
numbers = [3, 3, 4, 78, 9987, 0, 12, -46]
minimum = numbers[0] #Initialize the variable to store the minimum value, initially set the variable to zero
for i in numbers:
    if i < minimum:
        minimum = i
print(f"The smallest number is: {minimum}")
#Find the biggest number in a list
numbers = [45, 6, 47, 747, 774 , 4646, 6474, 454, 8, 363665666]
minimum = numbers[0]
for i in numbers:
    if i > minimum:
        minimum = i
print(f"The largest number is: {minimum}")
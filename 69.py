#Find the sum of all items in a dictionary
my_dict = {
    'a': 10,
    'b': 20,
    'c': 30
}

#initialize the variable
total_sum = 0

for i in my_dict.values():
    total_sum += i
print("Sum of all the items in the dictionary:", total_sum)
 
#Program to extract unique dictionary values
#sample dictionary
my_dict = {
    'a': 10,
    'b': 20,
    'c': 10,
    'd': 40,
    'e': 20,
}
#Initialize an empty set to store unique values
uni_val = set()

for i in my_dict.values():
    #Add each value to the set during iteration
    uni_val.add(i)

#Convert set to list
unique_values_list = list(uni_val)
print(f"Unique values in the dictionary: {unique_values_list}")
#Program to merge two dictionaries
dict1 = {'a' : 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

dict1.update(dict2)

print(f"Merged dictionary using (update()): {dict1}")
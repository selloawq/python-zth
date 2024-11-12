#Merge dictionaries using dictionary unpacking
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd':4}

merged_dict = {**dict1, **dict2}

print(f"Merged dictionary using (dictionary unpacking): {merged_dict}")
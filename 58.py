#Remove empty lists from List
list_of_lists = [[1,2,3], [], [6,7],[8],[34,6,88],[86],[]]
#Using a list comprehension to remove empty lists
filtered_list = [i for i in list_of_lists if i] 
print(f"List after removing the hollow shells: {filtered_list}")
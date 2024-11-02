#Find N largest elements from a list
def find_n_largest_elements(lst, n):
    #Sort the list in descending order
    sorted_lst =sorted(lst, reverse=True)
    #Get the first N elements
    largest_elements = sorted_lst[:n]
    return largest_elements
numbers = [34,34,34,3,35,54554,65745,646,56,436,6,45,6436646,546,45656456,456,5634,6,352,5,435]
N = int(input("N = "))
result = find_n_largest_elements(numbers, N)
print(f"The {N} largest elements are: {result}")
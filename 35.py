#Program to find the largest element in an array
def find_largest_element(arr):
    if not arr:
        return "Array is empty"
    #Initialize the first element as the largest
    largest_element = arr[0]

    #Iterate through the array to find the largest element
    for element in arr:
        if element > largest_element:
            largest_element = element
    return largest_element

my_array = [10,2,20,13,3,6,9,33,68,4,3,9,0,100]
result = find_largest_element(my_array)
print("The largest element in the array is:", result)
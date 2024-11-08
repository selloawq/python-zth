#A program to split the array and add the first part to the end(Rotation)
def split_and_add(arr, k):
    if k <= 0 or k >= len(arr):
        return arr
    
    #Split the array into two parts
    first_part = arr[:k]
    second_part = arr[k:]

    #Add first part to the end of the second part
    result = second_part + first_part
    return result

#test the function
arr = [1,2,3,4,5,6,7]
k = int(input("Input k rotation value: "))
result = split_and_add(arr, k)
print("Original Array:", arr)
print("Array after splitting and adding:", result)

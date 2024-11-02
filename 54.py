#Find the second largest number in a list
numbers = [4, 363, 636, 46, 57, 7, 58, 5252, 4333]
numbers.sort(reverse=True) #Sort the numbers in descending order
#Checking if there are atleast two elements in the list
if len(numbers) >= 2:
    second_largest = numbers[1]
    print(f"The second largest number is: {second_largest}")
else:
    print(f"This list does not contain a second largest number")
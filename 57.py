#Find odd numbers in a list
numbers = [54,55,6,6,456,34543,6,427,57,6,6,888,78,8,68,88,68,686,8658,68,4,6865,8658,65,8658,58,653,868,787,89,7,85,865,86,658,5]
odd_numbers = [num for num in numbers if num % 2 != 0]
print(f"The odd numbers in the list are: {odd_numbers}")
#Fin even numbers in a list
numbers = [44,43,434,554,575,6435,455,45,55,45,55,45,522,6,43,4,373,6,]
even_numbers = [num for num in numbers if num % 2 == 0]
print(f"Even number in list are: {even_numbers}")
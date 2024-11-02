#We wanna swap two variables###

#Input two variables
a = float(input("Enter the value of first variable: "))
b = float(input("Enter the valuse of the second variable: "))
#Display original values
print(f"Original values: a = {a}, b = {b}")
temp = a
a = b
b = temp
#Display swapped values
print(f"Swapped values: a = {a}, b = {b}")
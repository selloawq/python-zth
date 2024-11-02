#Swapping  without temp variable

a = float(input("Enter value for a: "))
b = float(input("Enter values for b: "))

a, b = b, a

print("After swapping")
print("a =", a)
print("b =", b)
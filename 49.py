#Print all pronic numbers between a certain range
def is_pronic_number(num):
    for n in range(1, int(num**0.5) + 1):
        if n * (n + 1) == num:
            return True
    return False
x = int(input("Enter start of range: "))
y = int(input("Enter end of range: "))
print(f"Pronic numbers between {x} and {y} are: ")
for i in range(x, y + 1):
    if is_pronic_number(i):
        print(i, end=" | ")
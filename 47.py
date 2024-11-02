#Print all the happy numbers within a certain range
def is_happy_number(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(i) ** 2 for i in str(num))
    return num == 1

happy_numbers = []
x = int(input("Enter beginning of range: "))
y = int(input("Enter the end of range: "))
for num in range(x, y + 1):
    if is_happy_number(num):
        happy_numbers.append(num)
print(f"Happy Numbers between {x} and {y}: {happy_numbers}")

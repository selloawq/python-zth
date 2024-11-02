#Division
num3 = float(input("Enter the dividend for division: "))
num4 = float(input("Enter the divisor for divison: "))
if num4 == 0:
    print("Error: Dividing by zero is not allowed")
else:
    div_result = num3 / num4
    print(f"Division: {num3} / {num4} = {div_result}")
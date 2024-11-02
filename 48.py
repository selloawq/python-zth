#Determine if a number is a Harshad Number
def is_harshad_number(num):
    #Calculate sum of the digits
    digit_sum = sum(int(i) for i in str(num))
    #Check if number is divisible by its total
    return num % digit_sum == 0

num = int(input("Enter a number: "))
if is_harshad_number(num):
    print(f"{num} is a Harshad Number")
else:
    print(f"{num} is not a Harshad Number")
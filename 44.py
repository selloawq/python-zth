#Check if number is a Disarium Number
def is_disarium(number):
    #Convert the number to a string to iterate over its digits
    num_str = str(number)

    #Calculate the sum of digits raised to their respective positions
    digit_sum = sum(int(i) ** (index + 1) for index, i in enumerate(num_str))

    #Check if sum is equal to original number
    return digit_sum == number

#Input a number from the user
try:
    num = int(input("Enter a number: "))

    #Check if its a disarium number
    if is_disarium(num):
        print(f"{num} is a Disarium number.")
    else:
        print(f"{num} is not a Disarium number.")
except ValueError:
    print("Invalid input. PLease enter a valid number") 
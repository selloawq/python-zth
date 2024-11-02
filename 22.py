#Finding Armstrong number in an interval
lower = int(input("Enter lower bound of interval: "))
upper = int(input("Enter the upper bound of the interval: "))

print("The Armstrong numbers are:", end=" ")

for num in range(lower, upper + 1):
    order = len(str(num)) #Find number of digits in 'num'
    temp_num = num
    sum = 0

    while temp_num > 0:
        digit = temp_num % 10
        sum += digit ** order
        temp_num //= 10

    #Check if 'num' is an Armstrong number
    if num == sum:
        print(num, end= " ")



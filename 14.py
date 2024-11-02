#Program to check LEap yeAr

year = int(input("Enter a year: "))
if (year % 400 == 0):
    #Divisible by 100 means century year (ending 00) and by 400 means leap year.
    print("{0} is a leap year".format(year))
#Not divisible by 100 means not century year however if divisible by 4 means leap year
elif (year % 4 == 0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))
#If not divisible by both 4 and 100 means not a leap year.
else:
    print("{0} is not a leap year".format(year))
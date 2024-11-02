#Check if a string contains any special character
import re
def check_special_char(in_str):
    #Define a regular expression pattern to match special characters
    pattern = r'[!@#$%^&*()_+{}\[\]:;<>,.?\\\/\'"\-=]'
    #Use re.search to find a match in the input string
    if re.search(pattern, in_str):
        return True
    else:
        return False
#Input a string
input_string = str(input("Enter a string: "))
contains_special = check_special_char(input_string)
#PRINT!
if contains_special:
    print("The string contains special characters.")
else:
    print("The string does not contain special characters.")
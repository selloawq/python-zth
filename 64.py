#Check if string is binary or not
def is_binary_str(input_str):
    for i in input_str:
        if i not in '01':
            return False
    return True #If all characters are '0' or '1', its a binary string
input_str = "1010101010"
if is_binary_str(input_str):
    print(f"{input_str} is a binary string")
else:
    print(f"{input_str} is not a binary string.")
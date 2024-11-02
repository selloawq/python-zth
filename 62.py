#Remove nth character from string
def remove_char(input_str, i):
    #Check if i is valid
    if i < 0 or i >= len(input_str):
        print(f"Invalid index {i}. The string remains unchanged.")
        return input_str
    #Remove nth character using slicing
    result_str = input_str[:i] + input_str[i + 1:]
    return result_str

#Input the string
input_str = input("Enter the string: ")
i = int(input("Enter character position to remove: "))
new_str = remove_char(input_str, i)
print(f"Original String: {input_str}")
print(f"String after removing {i}th character: {new_str}")
    


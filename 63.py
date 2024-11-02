#Split and join a string
input_str = "Python program to split and join a string"
word_list = input_str.split() #By default split on whitespace

#Join the list of words into a string
separator = " " #Specify the separator between words
output_str = separator.join(word_list)

#Print results
print(f"Original string: {input_str}")
print(f"List of split words: {word_list}")
print(f"Joined string: {output_str}")
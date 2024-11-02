#Sorting words by alphabetical order
my_str = input("Enter a string: ")

#Breakdown the string into a list of words
words = [word.capitalize() for word in my_str.split()]

#Sort the list
words.sort()

#Display sorted words
print("The sorted words are:")
for word in words:
    print(word)

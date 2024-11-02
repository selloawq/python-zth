# Define punctuation
punctuations = '''!()-\\[]{};:+'",<>./?@#$%^&*_~'''

# Take input from user
my_str = input("Enter a string: ")

# Remove punctuation
no_punct = ""
for char in my_str:
    if char not in punctuations:
        no_punct += char

# Display the unpunctuated string
print(no_punct)

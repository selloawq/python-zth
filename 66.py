#FInd all duplicate characters in a string
def find_duplicates(input_str):
    char_count = {}
    #Initialize a list to store duplicate characters
    duplicates = []
    #Iterate through each character
    for i in input_str:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1
    #Iterate through the dictionary and add characters with count > 1
    for i, count in char_count.items():
        if count > 1:
            duplicates.append(i)
    return duplicates

input_string = "piyushh sharma"
#Find duplicate characters
duplicate_chars = find_duplicates(input_string)
print("Duplicate characters:", duplicate_chars)

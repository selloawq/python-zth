#Find words greater than k length
def find_words(words, k):
    result = []
    #Iterate through each word in the list
    for i in words:
        if len(i) > k:
            result.append(i)
    return result
word_list = ["apple", "banana", "cherry", "date", "elderberry"]
k = int(input("Enter character length: "))
long_words = find_words(word_list, k)
print(f"Words longer than {k} characters: {long_words}")
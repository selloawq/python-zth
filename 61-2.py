def find_word(words, k):
    count = 0
    for i in words:
        if len(i) > k:
            count += 1
    return count
word_list = ["apple", "banana", "cherry", "date", "mom", "elderberry"]
k = int(input("Enter character length: "))
long_words_count = find_word(word_list, k)
print(f"Number of words longer than {k} characters are {long_words_count}")
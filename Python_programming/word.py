def count_words(string):
    words = string.split()
    return len(words)


input_string = input("")
word_count = count_words(input_string)
print("Number of words:", word_count)

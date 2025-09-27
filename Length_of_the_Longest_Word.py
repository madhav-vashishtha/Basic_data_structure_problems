sentence = input("Enter a sentence: ")

words = sentence.split()
max_length = max(len(word) for word in words)

print("Length of the longest word is:", max_length)

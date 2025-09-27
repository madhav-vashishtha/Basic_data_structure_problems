word1 = input("Enter first word: ")
word2 = input("Enter second word: ")


def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    return sorted(str1) == sorted(str2)

if is_anagram(word1, word2):
    print("They are anagrams!")
else:
    print("They are not anagrams.")

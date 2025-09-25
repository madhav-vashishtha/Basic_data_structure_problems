'''Palindrome wo word, number ya sequence hota hai jo ulta-pulta same ho'''

def is_palindromic_tuple(t):
    return t == t[::-1]

print(is_palindromic_tuple((1, 2, 3, 2, 1)))
print(is_palindromic_tuple((4, 5, 6)))
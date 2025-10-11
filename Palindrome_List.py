def is_palindrome(lst):
    return lst == lst[::-1]

print(is_palindrome([7, 8, 9, 8, 7]))
print(is_palindrome([1, 2, 3, 4, 5]))
print(is_palindrome([1, 2, 3, 2, 1]))

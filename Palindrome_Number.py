def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    
    s = str(x)
    rev = ""

    for ch in s:
        rev = ch + rev

    return s == rev 

print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))


def isPalindrome(s):
    result = ""

    for ch in s:
        if ch.isalnum():
            result += ch.lower()

    if result == result[::-1]:
        return True
    else:
        return False

print(isPalindrome("A man, a plan, a canal: Panama")) 
print(isPalindrome("race a car"))                    
print(isPalindrome(" "))                        



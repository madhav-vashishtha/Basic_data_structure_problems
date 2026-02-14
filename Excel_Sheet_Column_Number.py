def titleToNumber(columnTitle):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = 0
    
    for ch in columnTitle:
        value = alphabet.index(ch) + 1  
        result = result * 26 + value
    
    return result


print(titleToNumber("A"))   # 1
print(titleToNumber("AB"))  # 28
print(titleToNumber("ZY"))  # 701





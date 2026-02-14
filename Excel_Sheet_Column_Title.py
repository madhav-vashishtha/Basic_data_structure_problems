def convertToTitle(columnNumber):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    while columnNumber > 0:
        columnNumber -= 1         
        remainder = columnNumber % 26
        result = letters[remainder] + result
        columnNumber //= 26

    return result

print(convertToTitle(1))   
print(convertToTitle(28)) 
print(convertToTitle(701)) 




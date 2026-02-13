def alternateDigitSum(n):
    s = str(n)    
    total = 0
    sign = 1     
    
    for ch in s:
        total += sign * int(ch)
        sign *= -1  
    
    return total

print(alternateDigitSum(521))   
print(alternateDigitSum(111))  
print(alternateDigitSum(886996)) 



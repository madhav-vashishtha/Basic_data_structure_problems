def romantoint(s: str) -> int:
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,   
        'M': 1000
    }
    
    total = 0
    prev = 0
    
    for char in reversed(s):  
        value = roman_values[char]
        
        if value < prev:
            total -= value
        else:
            total += value
        
        prev = value
    
    return total

print(romantoint("XLV"))
print(romantoint("CCLXIV"))


def dayOfYear(date):
        
    year, month, day = map(int, date.split('-'))
    
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        days[1] = 29
    
    return sum(days[:month-1]) + day

print(dayOfYear("2023-11-19"))  
print(dayOfYear("2024-06-29")) 
print(dayOfYear("2025-03-09")) 

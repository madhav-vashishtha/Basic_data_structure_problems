from datetime import date
def dayOfTheWeek(day, month, year): 
    days = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]
    
    return days[date(year, month, day).weekday()]

print(dayOfTheWeek(19, 11, 2023))
print(dayOfTheWeek(29, 6, 2024))
print(dayOfTheWeek(9, 3, 2025))

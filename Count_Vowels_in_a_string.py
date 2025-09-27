text=input("enter a string: ")

def count_vowels(string):      
    vowels = "aeiouAEIOU"       
    count = 0                  
    for char in string:        
        if char in vowels:     
            count += 1         
    return count              

print("Number of vowels:", count_vowels(text))

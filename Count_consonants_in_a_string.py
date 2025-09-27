string = "Programming is fun"

def count_consonants(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch.isalpha() and ch not in vowels:  
            count += 1
    return count

print("Number of consonants:", count_consonants(string))

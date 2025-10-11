def nextGreatestLetter(letters, target):
    for ch in letters:
        if ch > target:
            return ch
    return letters[0]

print(nextGreatestLetter(['c', 'f', 'j'], 'k'))  
print(nextGreatestLetter(['c', 'f', 'j'], 'c'))  
print(nextGreatestLetter(['c', 'f', 'j'], 'a'))  

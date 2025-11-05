string = input("enter string: ")
vowels = "aeiouAEIOU"
newstring = ""
for chr in string:
    if chr in vowels:
        newstring += "*"
    else:
        newstring += chr 
    print(newstring)


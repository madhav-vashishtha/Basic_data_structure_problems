def findTheDifference(s, t):
    count = {}

    for ch in s:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

    for ch in t:
        if ch not in count:
            return ch
        elif count[ch] == 0:
            return ch
        else:
            count[ch] -= 1

s = "abcd"
t = "abcde"
print(findTheDifference(s, t))

s = ""
t = "y"
print(findTheDifference(s, t))


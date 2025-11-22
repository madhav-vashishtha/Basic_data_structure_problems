def longestCommonPrefix(strs):
    if not strs:
        return ""
    strs.sort()

    first = strs[0]
    last = strs[-1]
    prefix = ""
    for i in range(min(len(first) , len(last))):
        if first[i] == last[i]:
            prefix += first[i]
        else:
           break
    return prefix

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))


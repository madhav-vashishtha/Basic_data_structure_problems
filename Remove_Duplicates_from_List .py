'''Remove Duplicates from List (without set)
Input: [1,2,2,3,4,4,5] → Output: [1,2,3,4,5]'''

lst = [1, 2, 2, 3, 4, 4, 5]
result = list(dict.fromkeys(lst))
print(result)
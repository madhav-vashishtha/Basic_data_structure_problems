def search(nums , target):
    if target in nums:
        return nums.index(target)
    else:
        return -1

print(search([4, 5, 6, 7, 0, 1, 2], 0))
print(search([4, 5, 6, 7, 0, 1, 2], 3))  

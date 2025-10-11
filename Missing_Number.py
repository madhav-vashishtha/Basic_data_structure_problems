def missingNumber(nums):
    n = len(nums)
    total = n * (n + 1) // 2  
    return total - sum(nums)  

print(missingNumber([3, 0, 1]))     
print(missingNumber([0, 1]))         
print(missingNumber([8, 7, 6, 4, 3, 2, 0, 1]))

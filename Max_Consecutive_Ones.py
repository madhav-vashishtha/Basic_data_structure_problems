def find_max_consecutive_ones(nums):
    count = 0
    max_count = 0
    for num in nums:
        if num == 1:
            count += 1 
            max_count = max(max_count, count)
        else:
            count = 0 
    return max_count


print(find_max_consecutive_ones([0, 0, 0, 0])) 
print(find_max_consecutive_ones([1, 0, 1, 1, 0, 1, 1, 1, 1]))
print(find_max_consecutive_ones([1, 1, 0, 1, 1, 1]))
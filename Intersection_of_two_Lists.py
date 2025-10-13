def intersection (nums1, nums2):
    set1=set(nums1)
    set2=set(nums2)
    intersection=set1.intersection (set2)
    result=list(intersection)

    return result

print(intersection([1, 2, 3], [4, 5, 6]))
print(intersection([1, 2, 2, 1], [2, 2])) 
print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))

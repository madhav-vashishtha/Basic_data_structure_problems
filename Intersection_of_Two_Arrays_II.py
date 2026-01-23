def intersect(nums1, nums2):
    freq = {}
    result = []

    for num in nums1:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    for num in nums2:
        if num in freq and freq[num] > 0:
            result.append(num)
            freq[num] -= 1

    return result

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersect(nums1, nums2))

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(intersect(nums1, nums2))

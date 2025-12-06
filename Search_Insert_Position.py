def searchInsert( nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binary(l, r):
            if l > r:
                return l
        
            mid = (l + r) // 2
        
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binary(l, mid - 1)
            else:
                return binary(mid + 1, r)
    
        return binary(0, len(nums) - 1)
print(searchInsert([1,3,5,6], 5))
print(searchInsert([1,3,5,6], 2))
print(searchInsert([1,3,5,6], 7))


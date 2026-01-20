def findTheDistanceValue(arr1, arr2, d):
    count = 0
    for x in arr1:
        is_valid = True

        for y in arr2:
            if abs(x - y) <= d:
                is_valid = False
                break

        if is_valid:
            count += 1

    return count

arr1 = [4,5,8]
arr2 = [10,9,1,8]
d = 2
print(findTheDistanceValue(arr1, arr2, d))

arr1 = [2,1,100,3]
arr2 = [-5,-2,10,-3,7]
d = 6
print(findTheDistanceValue(arr1, arr2, d))
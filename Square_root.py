def mysqrt(x):
    
    if x == 0 or x == 1:
        return x
    
    low = 0
    high = x
    ans = 0

    while low <= high:
        mid = (low + high) // 2

        if mid * mid == x:
            return mid
        elif mid * mid < x:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans

print(mysqrt(8))
print(mysqrt(4))
print(mysqrt(2025))

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

print(is_sorted([5, 4, 3, 2, 1]))
print(is_sorted([1, 2, 3, 4, 5]))

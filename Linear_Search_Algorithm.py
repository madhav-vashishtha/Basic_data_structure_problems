def linear_search(arr, target):
    # Traverse the list element by element
    for i in range(len(arr)):
        if arr[i] == target:
            return i   # Return index if target found
    return -1          # Return -1 if target not found


print(linear_search([3, 7, 2, 5], 2))   # Output: 2
print(linear_search([1, 1, 2, 1], 1))   # Output: 0
print(linear_search([], 5))             # Output: -1
print(linear_search([4, 2, 8], 6))      # Output: -1

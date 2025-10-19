def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0, n-i-1):       # last i elements already sorted
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort([64, 25, 12, 22, 11]))
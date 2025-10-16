matrix = [[1, 3, 5, 7], 
           [10, 11, 16, 20], 
           [23, 30, 34, 60]]


def searchMatrix(matrix,target):
    if not matrix or not matrix[0]:
        return False
    m=len(matrix)
    n=len(matrix[0])
    for i in range(m*n):
        row=i // n
        col=i % n
        if matrix[row][col]==target:
            return True
    return False
print(searchMatrix(matrix, 13))  
print(searchMatrix(matrix, 3))  
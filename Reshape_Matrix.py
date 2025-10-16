def matrix_reshape(matrix,r,c):
    m=len(matrix)
    n=len(matrix[0])
    if m*n != r*c:
        return matrix
    flat= [num for row in matrix for num in row]
    
    reshape=[]
    for i in range(r):
         reshape.append(flat[i*c : (i+1)*c])
    
    return reshape

print(matrix_reshape([[1, 2], [3, 4]], 1, 4))
print(matrix_reshape([[1, 2], [3, 4]], 2, 4))  
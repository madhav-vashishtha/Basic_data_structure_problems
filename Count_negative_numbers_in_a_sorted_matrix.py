grid = [[4, 3, 2, 1],
        [3, 2, 1, -1],
        [1, 1, -1, -2],
        [-1, -1, -2, -3]]

def countNegatives(grid):
    count = 0
    for row in grid:
        for num in row:
            if num < 0:
                count += 1
    return count

print(countNegatives(grid)) 

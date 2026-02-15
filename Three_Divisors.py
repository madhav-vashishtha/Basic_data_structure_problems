def isThree(n: int) -> bool:
    root = int(n ** 0.5)
    if root * root != n:
        return False

    if root < 2:
        return False

    for i in range(2, int(root ** 0.5) + 1):
        if root % i == 0:
            return False

    return True

print(isThree(2)) 
print(isThree(4))
print(isThree(9))  
print(isThree(16)) 

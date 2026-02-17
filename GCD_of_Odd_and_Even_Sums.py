import math

def gcdOddEven(n):
    sumOdd = n * n
    sumEven = n * (n + 1)

    return math.gcd(sumOdd, sumEven)

print(gcdOddEven(4))
print(gcdOddEven(5))


def isUgly(n):
        if n <= 0:
            return False

        for p in (2, 3, 5):
                if n % p == 0:
                    n //= p

        return n == 1

print(isUgly(6))
print(isUgly(1)) 
print(isUgly(14)) 
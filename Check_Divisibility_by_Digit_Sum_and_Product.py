def checkDivisibility(n):
        digits = list(map(int, str(n)))

        digit_sum = sum(digits)

        digit_product = 1
        for d in digits:
            digit_product *= d

        total = digit_sum + digit_product

        return n % total == 0

print(checkDivisibility(99))
print(checkDivisibility(23))
print(checkDivisibility(45))
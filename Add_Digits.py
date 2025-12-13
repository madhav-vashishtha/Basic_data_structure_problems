def addDigits(num):
    if num == 0:
            return 0

        #[digital root=1+(num−1)mod9]

    return 1 + (num - 1) % 9

print(addDigits(38))
print(addDigits(45))
print(addDigits(264))
print(addDigits(0))


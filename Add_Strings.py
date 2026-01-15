def addStrings(num1: str, num2: str) -> str:
    digits = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
    }

    i = len(num1) - 1
    j = len(num2) - 1
    carry = 0
    result = []

    for _ in range(max(len(num1), len(num2))):
        d1 = digits[num1[i]] if i >= 0 else 0
        d2 = digits[num2[j]] if j >= 0 else 0

        total = d1 + d2 + carry
        result.append(str(total % 10))
        carry = total // 10

        i -= 1
        j -= 1

    if carry:
        result.append(str(carry))

    return ''.join(result[::-1])


print(addStrings("11", "123"))
print(addStrings("456", "77"))
print(addStrings("0", "0"))

def isPerfectSquare(num):
        left, right = 1, num

        for _ in range(32):
            mid = (left + right) // 2
            sq = mid * mid

            if sq == num:
                return True
            elif sq < num:
                left = mid + 1
            else:
                right = mid - 1

        return False

print(isPerfectSquare(16))
print(isPerfectSquare(14))
def addToArrayForm(num, k):
        res = []
        carry = k

        for i in range(len(num) - 1, -1, -1):
            carry += num[i]
            res.append(carry % 10)
            carry //= 10

        if carry > 0:  
            for d in str(carry) [::-1]:
                res.append(int(d))

        return res[::-1]

print(addToArrayForm([1,2,0,0],34))
print(addToArrayForm([2,7,4],181))
print(addToArrayForm([2,1,5],806))

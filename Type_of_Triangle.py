def triangleType(nums):
        
        a , b , c = nums 

        if a + b <= c or a + c <= b or b + c <= a:
            return "none"

        if a == b == c:
            return "equilateral"
        elif a == b or b == c or a == c:
            return "isosceles"
        else:
            return "scalene"
        
print(triangleType([3,3,3]))
print(triangleType([3,4,5]))
print(triangleType([1,2,3]))

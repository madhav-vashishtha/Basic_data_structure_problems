class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[:i+1]
        return ""

sol = Solution()
print(sol.largestOddNumber("52"))
print(sol.largestOddNumber("4206"))
print(sol.largestOddNumber("35427"))


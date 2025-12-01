class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a:
            return b
        if not b:
            return a
        
        if a[-1] == "0" and b[-1] == "0":
            return self.addBinary(a[:-1], b[:-1]) + "0"

        if a[-1] == "1" and b[-1] == "1":
            return self.addBinary(self.addBinary(a[:-1], "1"), b[:-1]) + "0"

        else:
            return self.addBinary(a[:-1], b[:-1]) + "1"

sol = Solution()
print(sol.addBinary("1010", "1011"))
print(sol.addBinary("11", "1"))

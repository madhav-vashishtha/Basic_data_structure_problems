class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set("aeiouAEIOU")
        s = list(s)

        v = [ch for ch in s if ch in vowels]

        v = v[::-1]

        idx = 0
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = v[idx]
                idx += 1

        return "".join(s)
sol = Solution()
print(sol.reverseVowels("IceCreAm"))   
print(sol.reverseVowels("leetcode"))  


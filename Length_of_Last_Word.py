class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        found = False
    
        for ch in reversed(s):
            if ch != ' ':
                count += 1
                found = True
            elif found:
                break
        return count

sol = Solution()
print(sol.lengthOfLastWord("Hello World"))
print(sol.lengthOfLastWord("   fly me   to   the moon  "))
print(sol.lengthOfLastWord("luffy is still joyboy"))

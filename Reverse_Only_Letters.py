def reverseOnlyLetters(s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)

        letters = [c for c in s if c.isalpha()][::-1]

        j = 0

        for i in range(len(s)):
            if s[i].isalpha():
                s[i] = letters[j]
                j += 1

        return "".join(s)

print(reverseOnlyLetters("ab-cd"))
print(reverseOnlyLetters( "a-bC-dEf-ghIj"))
print(reverseOnlyLetters("Test1ng-Leet=code-Q!"))


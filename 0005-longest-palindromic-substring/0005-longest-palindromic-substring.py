class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        ans = ""
        maxLen = 0
        for i in range(len(s)):
            a = i
            b = i
            while a >= 0 and b < len(s) and s[a] == s[b]:
                if b - a + 1 > maxLen:
                    maxLen = b - a + 1
                    ans = s[a:b+1]
                a -= 1
                b += 1
        for i in range(len(s)):
            a = i
            b = i + 1
            while a >= 0 and b < len(s) and s[a] == s[b]:
                if b - a + 1 > maxLen:
                    maxLen = b - a + 1
                    ans = s[a:b+1]
                a -= 1
                b += 1
        return ans
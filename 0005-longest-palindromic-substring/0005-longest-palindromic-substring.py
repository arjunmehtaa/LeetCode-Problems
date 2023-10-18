class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxLen = 0
        ans = ""
        
        for i in range(n):
            a = i
            b = i
            while a >= 0 and b < n and s[a] == s[b]:
                if b - a + 1 > maxLen:
                    maxLen = b - a + 1
                    ans = s[a:b+1]
                a -= 1
                b += 1
                
        for i in range(0, n-1):
            a = i
            b = i + 1
            while a >= 0 and b < n and s[a] == s[b]:
                if b - a + 1 > maxLen:
                    maxLen = b - a + 1
                    ans = s[a:b+1]
                a -= 1
                b += 1
                
        return ans
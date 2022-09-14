class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.maxLen = 0
        self.res = ""
                
        def traverse(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > self.maxLen:
                    self.maxLen = r - l + 1
                    self.res = s[l:r+1]
                l -= 1
                r += 1
                
        for i in range(len(s)):
            traverse(i, i)
            traverse(i, i + 1)
        
        return self.res
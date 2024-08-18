class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def palindrome(i, j):
            ans = 0
            while i >= 0 and j < len(s) and s[i] == s[j]:
                ans += 1
                i -= 1
                j += 1
            return ans
        
        ans = 0
        for i in range(len(s)):
            ans += palindrome(i, i)
            ans += palindrome(i, i + 1)
            
        return ans
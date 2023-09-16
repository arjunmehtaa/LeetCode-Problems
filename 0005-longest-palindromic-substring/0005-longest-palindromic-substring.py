class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen = 0
        ans = ""
        for i in range(len(s)):
            j = i
            k = i
            while j >= 0 and k < len(s) and s[j] == s[k]:
                if k - j + 1 > maxLen:
                    maxLen = k - j + 1
                    ans = s[j:k+1]
                j -= 1
                k += 1
        for i in range(len(s)):
            j = i
            k = i + 1
            while j >= 0 and k < len(s) and s[j] == s[k]:
                if k - j + 1 > maxLen:
                    maxLen = k - j + 1
                    ans = s[j:k+1]
                j -= 1
                k += 1
        return ans
                
                
        
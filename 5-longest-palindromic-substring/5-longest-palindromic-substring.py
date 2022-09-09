class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLength = 0
        answer = ""
        for i in range(len(s)):
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > maxLength:
                    maxLength = r - l + 1
                    answer = s[l : r + 1]
                l -= 1
                r += 1
        for i in range(len(s)):
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > maxLength:
                    maxLength = r - l + 1
                    answer = s[l : r + 1]
                l -= 1
                r += 1
        return answer
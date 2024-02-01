class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            a = i
            b = i
            while a >= 0 and b < len(s) and s[a] == s[b]:
                ans += 1
                a -= 1
                b += 1
            a = i
            b = i + 1
            while a >= 0 and b < len(s) and s[a] == s[b]:
                ans += 1
                a -= 1
                b += 1
        return ans
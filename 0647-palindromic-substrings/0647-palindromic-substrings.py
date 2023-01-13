class Solution:
    def countSubstrings(self, s: str) -> int:
        # if len(s) == 0:
        #     return 0
        # ans = len(s)
        # if len(s) > 1:
        #     for i in range(0, len(s) - 1):
        #         if s[i] == s[i+1]:
        #             ans += 1
        ans = 0
        for i in range(len(s)):
            a = i
            b = i
            while a >= 0 and b < len(s) and s[a] == s[b]:
                a -= 1
                b += 1
                ans += 1
            a = i
            b = i + 1
            while a >= 0 and b < len(s) and s[a] == s[b]:
                a -= 1
                b += 1
                ans += 1
        return ans
                    
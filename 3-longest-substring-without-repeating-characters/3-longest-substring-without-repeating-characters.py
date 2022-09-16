class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        a = 0
        res = 0
        for b in range(len(s)):
            if s[b] in map and map[s[b]] >= a:
                a = map[s[b]] + 1
            map[s[b]] = b
            res = max(res, b - a + 1)
        return res
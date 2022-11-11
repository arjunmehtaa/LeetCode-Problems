class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        a = 0
        b = 0
        ans = 0
        while b < len(s):
            if s[b] in map and map[s[b]] >= a:
                a = map[s[b]] + 1
            map[s[b]] = b
            ans = max(ans, b - a + 1)
            b += 1
        return ans
            
        
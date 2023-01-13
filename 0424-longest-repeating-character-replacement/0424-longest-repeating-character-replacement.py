class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        a = 0
        ans = 0
        map1 = {}
        for b in range(0, len(s)):
            map1[s[b]] = map1.get(s[b], 0) + 1
            while (b - a + 1) - max(map1.values()) > k:
                map1[s[a]] -= 1
                a += 1
            ans = max(ans, b - a  + 1)
        return ans 
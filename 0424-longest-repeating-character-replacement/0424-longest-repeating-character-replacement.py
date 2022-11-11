class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        a = 0
        ans = 0
        map = {}
        for b in range(len(s)):
            map[s[b]] = map.get(s[b], 0) + 1
            while (b - a + 1) - max(map.values()) > k:
                map[s[a]] -= 1
                a += 1
            ans = max(ans, b - a + 1)
        return ans
        
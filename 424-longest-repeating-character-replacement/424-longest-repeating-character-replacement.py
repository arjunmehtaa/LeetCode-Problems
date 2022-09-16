class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        a = 0
        map = {}
        for b in range(0, len(s)):
            map[s[b]] = map.get(s[b], 0) + 1
            while b - a + 1 - max(map.values()) > k:
                map[s[a]] -= 1
                a += 1
            res = max(res, b - a + 1)
        return res
        
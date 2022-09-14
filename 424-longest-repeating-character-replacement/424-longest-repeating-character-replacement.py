class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countMap = {}
        a = 0
        res = 0
        for b in range(len(s)):
            countMap[s[b]] = countMap.get(s[b], 0) + 1
            while (b - a + 1) - max(countMap.values()) > k:
                countMap[s[a]] -= 1
                a += 1
            res = max(res, b - a + 1)
        return res
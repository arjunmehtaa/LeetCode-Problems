class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        a = 0
        seen = {}
        for b in range(len(s)):
            seen[s[b]] = seen.get(s[b], 0) + 1
            while (b - a + 1) - max(seen.values()) > k:
                seen[s[a]] -= 1
                a += 1
            ans = max(ans, b - a + 1)
        return ans
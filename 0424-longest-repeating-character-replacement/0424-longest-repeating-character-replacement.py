class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        l = 0
        ans = 0
        for r in range(len(s)):
            seen[s[r]] = seen.get(s[r], 0) + 1
            while (r - l + 1) - max(seen.values()) > k:
                seen[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans
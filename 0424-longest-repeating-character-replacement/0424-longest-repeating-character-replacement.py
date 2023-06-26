class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        seen = {}
        i = 0
        for j in range(len(s)):
            seen[s[j]] = seen.get(s[j], 0) + 1
            while (j - i + 1) - max(seen.values()) > k:
                seen[s[i]] -= 1
                i += 1
            ans = max(ans, j - i + 1)
        return ans
                    
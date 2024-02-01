class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = {}
        for i in range(len(s)):
            seen[s[i]] = seen.get(s[i], 0) + 1
        for i in range(len(t)):
            if t[i] not in seen:
                return False
            seen[t[i]] -= 1
            if seen[t[i]] == 0:
                del seen[t[i]]
        return len(seen) == 0
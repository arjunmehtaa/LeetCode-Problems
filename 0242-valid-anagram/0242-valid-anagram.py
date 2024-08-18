class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        if len(s) != len(t):
            return False
        for c in s:
            seen[c] = seen.get(c, 0) + 1
        for c in t:
            if c not in seen:
                return False
            seen[c] -= 1
            if seen[c] == 0:
                del seen[c]
        return len(seen) == 0
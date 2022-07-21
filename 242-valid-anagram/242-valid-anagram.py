class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        set = {}
        for i in range(0, len(s)):
            if s[i] not in set:
                set[s[i]] = 0
            set[s[i]] += 1
            if t[i] not in set:
                set[t[i]] = 0
            set[t[i]] -= 1
        for i in range(0, len(s)):
            if set[s[i]] != 0:
                return False
        return True
        
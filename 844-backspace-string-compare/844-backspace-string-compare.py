class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a = ""
        b = ""
        for i in range(0, len(s)):
            if s[i] == "#":
                a = a[:-1]
            else:
                a += s[i]
        for j in range(0, len(t)):
            if t[j] == "#":
                b = b[:-1]
            else:
                b += t[j]
        if a == b:
            return True
        return False
        
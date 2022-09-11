class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a = len(s) - 1
        b = len(t) - 1
        while a >= 0 or b >= 0:
            if s[a] == "#":
                count = 2
                while count > 0:
                    count -= 1
                    a -= 1
                    if a >= 0 and s[a] == "#":
                        count += 2
            if t[b] == "#":
                count = 2
                while count > 0:
                    count -= 1
                    b -= 1
                    if b >= 0 and t[b] == "#":
                        count += 2
            if a >= 0 and b >= 0:
                if s[a] != t[b]:
                    return False
                a -= 1
                b -= 1
            elif a < 0 and b < 0:
                return True
            else:
                return False
        return True
            
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a = len(s) - 1
        b = len(t) - 1
        while a >= 0 or b >= 0:
            if a >= 0 and s[a] == "#":
                steps = 2
                while steps > 0:
                    a -= 1
                    steps -= 1
                    if a >= 0 and s[a] == "#":
                        steps += 2
            if b >= 0 and t[b] == "#":
                steps = 2
                while steps > 0:
                    b -= 1
                    steps -=  1
                    if b >= 0 and t[b] == "#":
                        steps += 2
            if a >= 0 and b >= 0:
                if s[a] != t[b]:
                    return False
                else:
                    a -= 1
                    b -= 1
            elif a < 0 and b < 0:
                return True
            else:
                return False
        return True
                    
                
        
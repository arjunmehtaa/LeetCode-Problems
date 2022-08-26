class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        x = generateString(s)
        y = generateString(t)
        if x == y:
            return True
        return False
        
def generateString(s):
    a = ""
    for i in range(0, len(s)):
        if s[i] == "#":
            a = a[:-1]
        else:
            a += s[i]
    return a
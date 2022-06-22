class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        x = generateString(s)
        y = generateString(t)
        if  x == y:
            return True
        return False
    
def generateString(string: str) -> str:
        a = ""
        for i in range(0, len(string)):
            if string[i] == "#":
                a = a[:-1]
            else:
                a += string[i]
        return a
dataMap = {'}':'{', ')':'(', ']':'['}

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in dataMap:
                if len(stack) == 0 or not stack.pop() == dataMap[char]:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0
        
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        charMap = {
            "(" : ")", 
            "{" : "}",
            "[" : "]"
        }
        for char in s:
            if char in charMap:
                stack.append(charMap[char])
            else:
                if len(stack) == 0 or char != stack.pop():
                    return False
        return len(stack) == 0
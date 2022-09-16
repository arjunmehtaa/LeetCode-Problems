class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {"}":"{", ")":"(", "]":"["}
        for char in s:
            if char in map:
                if len(stack) < 1 or map[char] != stack.pop():
                    return False
            else:
                stack.append(char)
        return len(stack) == 0
            
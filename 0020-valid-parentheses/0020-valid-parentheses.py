map = {"{":"}", "[":"]", "(":")"}

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in map:
                stack.append(map[char])
            else:
                if len(stack) == 0 or char != stack.pop():
                    return False
        return len(stack) == 0
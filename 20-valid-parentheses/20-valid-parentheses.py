map = {")":"(", "}":"{", "]":"["}

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(0, len(s)):
            if s[i] in map:
                if len(stack) == 0 or stack.pop() != map[s[i]]:
                    return False
            else:
                stack.append(s[i])
        return len(stack) == 0
        
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
        if len(stack) > 0:
            return False
        return True
        
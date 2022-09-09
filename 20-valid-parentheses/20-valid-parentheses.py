# Time Complexity   : O(N)
# Space Complexity  : O(N)

class Solution:
    def isValid(self, s: str) -> bool:
        map = {']':'[', '}':'{', ')':'('}
        stack = []
        for char in s:
            if char in map.values():
                stack.append(char)
            else:
                if len(stack) == 0 or stack.pop() != map[char]:
                    return False
        return len(stack) == 0

class Solution:
    def isValid(self, s: str) -> bool:
        bracketsMap = {
            ")" : "(", 
            "}" : "{", 
            "]" : "["
        }
        stack = []
        for char in s:
            if char in bracketsMap:
                if len(stack) == 0 or stack.pop() != bracketsMap[char]:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0
        
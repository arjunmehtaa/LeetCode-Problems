class Solution:
    def isValid(self, s: str) -> bool:
        
        p_map = {
            "]": "[", 
            ")": "(", 
            "}": "{"
        }
        stack = []
        
        for c in s:
            if c in p_map:
                if len(stack) == 0 or stack.pop() != p_map[c]:
                    return False
            else:
                stack.append(c)
                
        return len(stack) == 0
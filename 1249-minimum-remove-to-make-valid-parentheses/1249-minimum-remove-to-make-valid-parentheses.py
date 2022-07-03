# Time Complexity   : O(N)
# Space Complexity  : O(N)

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        i = 0
        stack = []
        while i < len(s):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if len(stack) > 0:
                    stack.pop()
                else:
                    s = s[:i] + s[i+1:]
                    i -= 1
            i += 1
        while len(stack) > 0:
            pos = stack.pop()
            s = s[:pos] + s[pos+1:]
        return s

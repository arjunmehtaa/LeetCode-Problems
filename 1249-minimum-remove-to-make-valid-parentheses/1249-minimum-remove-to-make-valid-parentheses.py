class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        answer = ""
        for i in range(0, len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if len(stack) > 0 and s[stack[-1]] != ")":
                    stack.pop()
                else:
                    stack.append(i)
        for i in range(0, len(s)):
            if i not in stack:
                answer += s[i]
        return answer
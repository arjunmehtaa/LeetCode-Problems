class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        for x in s:
            if x == '(' or x == '{' or x == '[':
                my_stack.append(x)
            else:
                if len(my_stack) == 0:
                    return False
                if x == ')':
                    value = my_stack.pop()
                    if value != '(':
                        return False
                elif x == '}':
                    value = my_stack.pop()
                    if value != '{':
                        return False
                elif x == ']':
                    value = my_stack.pop()
                    if value != '[':
                        return False
        if len(my_stack) == 0:
            return True
        else:
            return False
                    
        
dict = {}
dict[')'] = '('
dict[']'] = '['
dict['}'] = '{'

class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        for x in s:
            if x == '(' or x == '{' or x == '[':
                my_stack.append(x)
            else:
                if len(my_stack) == 0:
                    return False
                value = my_stack.pop()
                if value != dict[x]:
                    return False
        if len(my_stack) == 0:
            return True
        else:
            return False

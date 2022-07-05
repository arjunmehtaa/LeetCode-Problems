class MyQueue:
        
    stack = []
    reverse_stack = []
    
    def __init__(self):
        self.stack = []
        self.reverse_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        stack = self.stack
        reverse_stack = self.reverse_stack
        while len(stack) > 0:
            reverse_stack.append(stack.pop())
        value = reverse_stack.pop()
        while len(reverse_stack) > 0:
            stack.append(reverse_stack.pop())
        return value

    def peek(self) -> int:
        stack = self.stack
        reverse_stack = self.reverse_stack
        while len(stack) > 0:
            reverse_stack.append(stack.pop())
        value = reverse_stack[len(reverse_stack)-1]
        while len(reverse_stack) > 0:
            stack.append(reverse_stack.pop())
        return value

    def empty(self) -> bool:
        if len(self.stack) == 0:
            return True
        else:
            return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
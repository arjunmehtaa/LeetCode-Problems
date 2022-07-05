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
        if len(reverse_stack) == 0:
            while len(stack) > 0:
                reverse_stack.append(stack.pop())
        return reverse_stack.pop()

    def peek(self) -> int:
        stack = self.stack
        reverse_stack = self.reverse_stack
        if len(reverse_stack) == 0:
            while len(stack) > 0:
                reverse_stack.append(stack.pop())
        return reverse_stack[len(reverse_stack)-1]

    def empty(self) -> bool:
        return len(self.stack) == 0 and len(self.reverse_stack) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
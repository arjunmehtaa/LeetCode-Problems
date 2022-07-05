# Time Complexity   : O(N)
# Space Complexity  : O(N)

class MyQueue:
        
    stack = []
    reverse = []
    
    def __init__(self):
        self.stack = []
        self.reverse = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if len(self.reverse) == 0:
            while len(self.stack) > 0:
                self.reverse.append(self.stack.pop())
        return self.reverse.pop()

    def peek(self) -> int:
        if len(self.reverse) == 0:
            while len(self.stack) > 0:
                self.reverse.append(self.stack.pop())
        return self.reverse[len(self.reverse)-1]

    def empty(self) -> bool:
        return len(self.stack) == 0 and len(self.reverse) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
class MyQueue:

    def __init__(self):
        self.stack_front = []
        self.stack_back = []

    def push(self, x: int) -> None:
        while self.stack_front:
            self.stack_back.append(self.stack_front.pop())
        self.stack_back.append(x)

    def pop(self) -> int:
        while self.stack_back:
            self.stack_front.append(self.stack_back.pop())
        return self.stack_front.pop()

    def peek(self) -> int:
        while self.stack_back:
            self.stack_front.append(self.stack_back.pop())
        return self.stack_front[-1]

    def empty(self) -> bool:
        return not bool(self.stack_back or self.stack_front)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
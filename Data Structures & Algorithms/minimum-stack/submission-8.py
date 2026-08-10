class MinStack:

    def __init__(self):
        self.stack = []
        self.minEl = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minEl or val <= self.minEl[-1]:
            self.minEl.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.minEl[-1]:
            self.minEl.pop()
        self.stack.pop()        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minEl[-1]
        

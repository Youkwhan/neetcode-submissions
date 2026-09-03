class MinStack:

    def __init__(self):
        self.minStack = []

    def push(self, val: int) -> None:
        if not self.minStack:
            self.minStack.append((val, val))
        else:
            lastMin = self.getMin()
            self.minStack.append((min(val,lastMin), val))

    def pop(self) -> None:
        if not self.minStack:
            return
        self.minStack.pop()
        

    def top(self) -> int:
        if self.minStack:
            return self.minStack[-1][1]

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1][0]

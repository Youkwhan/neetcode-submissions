class MinStack:

    def __init__(self):
        self.min_stack = [] 
        

    def push(self, val: int) -> None:
        if not self.min_stack:
            self.min_stack.append((val,val))
        else:
            last_min = self.getMin()
            self.min_stack.append((min(val,last_min),val))

    def pop(self) -> None:
        if not self.min_stack:
            return
        self.min_stack.pop()
        

    def top(self) -> int:
        if self.min_stack:
            return self.min_stack[-1][1]
        

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1][0]

        

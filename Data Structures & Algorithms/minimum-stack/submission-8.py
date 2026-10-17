class MinStack:

    def __init__(self):
        self.stack=deque()
        self.minimum=0

    def push(self, val: int) -> None:
        if len(self.stack)==0:
            self.minimum=val
        self.stack.append(self.minimum-val)
        self.minimum=min(self.minimum,val)
    def pop(self) -> None:
        y=self.stack.pop()
        if y>0:
            self.minimum=self.minimum+y

    def top(self) -> int:
        
        y=self.stack[-1]
        if y>0:
            return self.minimum
        else:
            return self.minimum-y

    def getMin(self) -> int:
        return self.minimum
        

class MinStack:

    def __init__(self):
        self.stack=[]
    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min=val
        else:
            self.stack.append(val-self.min)
            if val<self.min:
                self.min=val
    def pop(self) -> None:
        popped= self.stack.pop()
        if popped<0:
            #self.min here is the old one just erased which should be the val in popped
            #So to retrieve the previous self.min we use the fact that we have self.min
            self.min=self.min -popped
            #Here we have technically currentself.min-(currentself.min-previousself.min)

    def top(self) -> int:
        top = self.stack[-1]
        if top>0:
            return top+self.min 
            #Remember to decode (val-self.min+self.min=val)
            # But only if we have positive
        else:
            #Because we have changed the self.min in this case
            return self.min 
    def getMin(self) -> int:
        return self.min
        

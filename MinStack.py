class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        INT_MAX=2**32
        self.stack=list()
        self.min=INT_MAX

    def push(self, x: int) -> None: 
        self.stack.append((x,self.min))
        if x<self.min:
            self.min=x

    def pop(self) -> None:
        self.min=self.stack.pop()[1]
        
    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.min
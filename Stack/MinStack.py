class MinStack:

    def __init__(self):
        self.data = []

    def push(self, val: int) -> None:
        if self.data:
            self.data.append((val, min(val, self.data[-1][1])))
        else:
            self.data.append((val,val))

    def pop(self) -> None:
        return self.data.pop()[0]

    def top(self) -> int:
        return self.data[-1][0]

    def getMin(self) -> int:
        return self.data[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

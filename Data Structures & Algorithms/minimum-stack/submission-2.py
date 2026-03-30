class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append((val,val))
            return
        prev = self.stack[-1][1]
        if prev < val:
            self.stack.append((val,prev))  
        else:
            self.stack.append((val,val))
        return None

    def pop(self) -> None:
        if len(self.stack) == 0:
            return None
        else:
            self.stack.pop()

    def top(self) -> int:
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1][0]

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return None
        else:
            return int((self.stack[-1])[1])
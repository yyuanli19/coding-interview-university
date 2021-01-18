"""
    this is cheating because array indexing is used
    Runtime: 196 ms, faster than 13.49% of Python3 online submissions for Design a Stack With Increment Operation.
    Memory Usage: 14.8 MB, less than 92.96% of Python3 online submissions for Design a Stack With Increment Operation.
"""
class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.start = 0
        self.size = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.size:
            self.stack.append(x)
        

    def pop(self) -> int:
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        start = min(len(self.stack), k)
        for i in range(start):
            self.stack[i] += val
        print(self.stack)
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

"""
    amazing lazy increment
"""
def __init__(self, maxSize):
    self.n = maxSize
    self.stack = []
    self.inc = []

def push(self, x):
    if len(self.inc) < self.n:
        self.stack.append(x)
        self.inc.append(0)

def pop(self):
    if not self.inc: return -1
    if len(self.inc) > 1:
        self.inc[-2] += self.inc[-1]
    return self.stack.pop() + self.inc.pop()

def increment(self, k, val):
    if self.inc:
        self.inc[min(k, len(self.inc)) - 1] += val

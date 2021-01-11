# according to solution
# head = (head + 1) % size; or end = (end + 1) % size
# is better then the incremental head/end while checking if it reaches the end
class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.len = 0
        self.start = -1
        self.end = -1
        self.queque = [0 for _ in range(k)]
        
    def enQueue(self, value: int) -> bool:
        # print(self.start, self.end, self.queque)
        if self.isFull():
            return  False
        if self.end == self.size-1:
            self.end = 0
        else:
            self.end += 1
        self.queque[self.end] = value
        self.len += 1
        
        if self.start == -1:
            self.start = 0
        return True

    def deQueue(self) -> bool:
        # print(self.start, self.end, self.queque)
        val = self.Front()
        if val == -1:
            return False
        self.len -= 1
        if self.len == 0:
            self.start = -1
            self.end = -1
            
        if self.start == self.size-1:
            self.start = 0
        else:
            self.start += 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queque[self.start]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queque[self.end]

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()





class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queque = []
        self.back_queque = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queque.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        self.top()
        return self.queque.pop(0)
            

    def top(self) -> int:
        """
        Get the top element.
        """
        if not self.queque:
            self.back_queque, self.queque = self.queque, self.back_queque
        # print(self.queque, self.back_queque)
        while len(self.queque) > 1:
            self.back_queque.append(self.queque.pop(0))
        #self.queque, self.back_queque = self.back_queque, self.queque
        return self.queque[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        # print(len(self.queque), self.queque)
        # print(len(self.back_queque), self.back_queque)
        return (len(self.queque)==0)&(len(self.back_queque)==0 )


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

"""
Runtime: 248 ms, faster than 70.04% of Python3 online submissions for Design Linked List.
Memory Usage: 14.8 MB, less than 80.28% of Python3 online submissions for Design Linked List.
"""
class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.length = 0
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if self.length <= index:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        # print("addAtHead")
        new_head = Node(val)
        new_head.next = self.head
        self.head = new_head
        self.length += 1
        # self.print()
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        # print("addAtTail")
        curr = self.head
        # print("curr: ", curr.val, curr.next)
        if curr is None:
            self.head = Node(val)
        else:
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(val)
        self.length += 1
        # self.print()
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            self.addAtHead(val)
            
        elif self.length < index:
            return
        else:
            # print("addAtIndex")
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            new_node = Node(val)
            new_node.next = curr.next
            curr.next = new_node
            self.length += 1
        # self.print()
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if self.length <= index:
            return
        else:
            # print("deleteAtIndex")
            curr = self.head
            if index == 0:
                self.head = curr.next
            else:
                for _ in range(index - 1):
                    curr = curr.next
                curr.next = curr.next.next
            self.length -= 1
        # self.print()
            
    def print(self):
        print("     print")
        if self.head is not None:
            curr = self.head
            print(curr.val)
            while curr.next is not None:
                curr = curr.next
                print(curr.val)
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

"""
doubly linked list
Runtime: 304 ms, faster than 33.76% of Python3 online submissions for Design Linked List.
Memory Usage: 15.6 MB, less than 10.24% of Python3 online submissions for Design Linked List.
"""
class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.length = 0
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if self.length <= index:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        # print("addAtHead")
        new_head = Node(val)
        new_head.next = self.head
        if self.head is not None:
            self.head.prev = new_head
        self.head = new_head
        self.length += 1
        # self.print()
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        # print("addAtTail")
        curr = self.head
        # print("curr: ", curr.val, curr.next)
        if curr is None:
            # by default
            self.addAtHead(val)
            # self.head = Node(val)
        else:
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(val)
            curr.next.prev = curr
            
        self.length += 1
        # self.print()
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if self.length < index:
            return
        elif index == 0:
            self.addAtHead(val)
        elif self.length == index:
            self.addAtTail(val)
        else:
            # print("addAtIndex")
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            new_node = Node(val)
            
            new_node.next = curr.next
            new_node.prev = curr
            curr.next.prev = new_node
            curr.next = new_node
            
            self.length += 1
        # self.print()
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if self.length <= index:
            return
        else:
            # print("deleteAtIndex", index)
            curr = self.head
            if index == 0:
                self.head = curr.next
                if self.head is not None:
                    self.head.prev = None
            elif index == self.length-1:
                for _ in range(index - 1):
                    curr = curr.next
                curr.next = None
            else:
                for _ in range(index - 1):
                    curr = curr.next
                # print("current cur", curr.val, curr.next.val)
                # if curr.next.next is not None:
                curr.next.next.prev = curr
                curr.next = curr.next.next
            self.length -= 1
        # self.print()
            
    def print(self):
        print("     print")
        if self.head is not None:
            curr = self.head
            print(curr.val)
            while curr.next is not None:
                curr = curr.next
                print(curr.val)
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

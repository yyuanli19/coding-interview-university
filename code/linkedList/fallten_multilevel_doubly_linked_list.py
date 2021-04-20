
"""
Runtime: 36 ms, faster than 61.41% of Python3 online submissions for Flatten a Multilevel Doubly Linked List.
Memory Usage: 14.6 MB, less than 82.12% of Python3 online submissions for Flatten a Multilevel Doubly Linked List.
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        curr = head
        while curr:
            # print(curr.val)
            if not curr.child:
                # go to the next
                curr = curr.next
            else:
                child = curr.child
                while child.next:
                    child = child.next
                child.next = curr.next
                if curr.next:
                    curr.next.prev = child
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None
        return head

        

"""
Runtime: 32 ms, faster than 85.46% of Python3 online submissions for Copy List with Random Pointer.
Memory Usage: 14.8 MB, less than 85.19% of Python3 online submissions for Copy List with Random Pointer.
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dummy=Node(0)
        dummy.next=head
        curr=head
        while head:
            new_node = Node(head.val)
            new_node.next = head.next
            head.next = new_node
            head = head.next.next
        
        while curr and curr.next:
            # print("curr", curr.val)
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
            
        new_head = dummy
        while new_head and new_head.next:
            # print(new_head.val)
            new_head.next = new_head.next.next
            new_head = new_head.next
            
        return dummy.next
    
            
         

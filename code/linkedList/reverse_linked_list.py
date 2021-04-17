"""
recursive solution
Runtime: 32 ms, faster than 85.38% of Python3 online submissions for Reverse Linked List.
Memory Usage: 15.6 MB, less than 75.15% of Python3 online submissions for Reverse Linked List.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return
        new_head = head
        while head.next is not None:
            curr = head.next
            # print(head.val, curr.val)
            head.next = curr.next
            curr.next = new_head
            new_head = curr

        return new_head
        
"""
official recursive solution
Runtime: 28 ms, faster than 95.83% of Python3 online submissions for Reverse Linked List.
Memory Usage: 19.1 MB, less than 6.64% of Python3 online submissions for Reverse Linked List.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last

        
        

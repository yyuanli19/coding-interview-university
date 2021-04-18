"""
Runtime: 72 ms, faster than 40.32% of Python3 online submissions for Remove Linked List Elements.
Memory Usage: 17.3 MB, less than 23.84% of Python3 online submissions for Remove Linked List Elements.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return
        dummy = ListNode(0)
        dummy.next = head
        
        curr = dummy
        while curr.next is not None:
            # print(curr.val)
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next
        

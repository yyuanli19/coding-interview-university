"""
simple solution that gets the length of the linked list first
Runtime: 52 ms, faster than 5.55% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 14.2 MB, less than 48.70% of Python3 online submissions for Remove Nth Node From End of List.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = 0
        curr = head
        while curr is not None:
            curr = curr.next
            length += 1
        # print(length)
        curr = head
        idx_front = length - n
        if idx_front == 0:
            head = head.next
        else:
            for _ in range(idx_front-1):
                curr = curr.next
            curr.next = curr.next.next
        return head
        
"""
official two pointer solution
Runtime: 32 ms, faster than 74.66% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 14.4 MB, less than 15.13% of Python3 online submissions for Remove Nth Node From End of List.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow, fast = head, head
        for _ in range(n+1):
            if fast is None:
                return head.next
            fast = fast.next
        
        while fast is not None:
            slow = slow.next
            fast = fast.next
        # print(slow.val)

        slow.next = slow.next.next
        return head
            
            
        
        

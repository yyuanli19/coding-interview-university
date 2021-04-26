"""
Runtime: 36 ms, faster than 90.42% of Python3 online submissions for Remove Duplicates from Sorted List II.
Memory Usage: 14.3 MB, less than 61.00% of Python3 online submissions for Remove Duplicates from Sorted List II.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(-101)
        dummy.next = head
        
        prev, curr = dummy, dummy.next
        while curr:
            if curr.next and curr.val == curr.next.val:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next
            
        return dummy.next

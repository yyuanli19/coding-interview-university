"""
Runtime: 52 ms, faster than 53.16% of Python3 online submissions for Linked List Cycle II.
Memory Usage: 17.2 MB, less than 80.63% of Python3 online submissions for Linked List Cycle II.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return
        slow, fast = head, head
        cycle = False
        while fast is not None and fast.next is not None:
            # print(slow.val, fast.val)
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                cycle = True
                break
        if cycle:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
        return
        

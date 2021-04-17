"""
Runtime: 80 ms, faster than 7.73% of Python3 online submissions for Linked List Cycle.
Memory Usage: 17.6 MB, less than 46.88% of Python3 online submissions for Linked List Cycle.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        slow, fast = head, head
        while True:
            if fast is None or fast.next is None:
                return False
            # print(slow.val, fast.val)
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        



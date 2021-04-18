"""
Runtime: 68 ms, faster than 71.70% of Python3 online submissions for Add Two Numbers.
Memory Usage: 14.4 MB, less than 12.03% of Python3 online submissions for Add Two Numbers.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        floating_number = 0
        dummy = ListNode(0)
        head = dummy
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            curr_sum = x + y + floating_number
            # print("curr_sum", curr_sum)
            if curr_sum > 9:
                curr_sum -= 10
                floating_number = 1
            else:
                floating_number = 0
            dummy.next = ListNode(curr_sum)
            dummy = dummy.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if floating_number == 1:
            dummy.next = ListNode(1)
        
        return head.next
            
        

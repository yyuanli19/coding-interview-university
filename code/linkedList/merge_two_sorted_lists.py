"""
    Runtime: 36 ms, faster than 75.07% of Python3 online submissions for Merge Two Sorted Lists.
    Memory Usage: 14.4 MB, less than 31.15% of Python3 online submissions for Merge Two Sorted Lists.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        root = ListNode(None)
        node = root
        while l1 and l2:
            if l1.val<l2.val:
                node.val = l1.val
                l1 = l1.next
            else:
                node.val = l2.val
                l2 = l2.next
            node.next = ListNode(None)
            node = node.next
        if l1:
            node.val = l1.val
            node.next = l1.next
        if l2:
            node.val = l2.val
            node.next = l2.next
        return root

"""
    Runtime: 32 ms, faster than 91.67% of Python3 online submissions for Merge Two Sorted Lists.
    Memory Usage: 14.3 MB, less than 31.15% of Python3 online submissions for Merge Two Sorted Lists.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2
        if l1.val<l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
 

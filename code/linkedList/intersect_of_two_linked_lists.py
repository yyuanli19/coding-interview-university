"""
simple hash set solution
Runtime: 152 ms, faster than 94.22% of Python3 online submissions for Intersection of Two Linked Lists.
Memory Usage: 29.9 MB, less than 7.32% of Python3 online submissions for Intersection of Two Linked Lists.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodes_seen = set()
        while headA is not None:
            nodes_seen.add(headA)
            headA = headA.next
        
        while headB is not None:
            if headB in nodes_seen:
                return headB
            headB = headB.next
        return

"""
official two pointer solution
Runtime: 160 ms, faster than 74.28% of Python3 online submissions for Intersection of Two Linked Lists.
Memory Usage: 29.2 MB, less than 95.31% of Python3 online submissions for Intersection of Two Linked Lists.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA, pB = headA, headB
        
        while pA != pB:
            if pA is None:
                pA = headB
            else:
                pA = pA.next
            
            if pB is None:
                pB = headA
            else:
                pB = pB.next
        return pA
            

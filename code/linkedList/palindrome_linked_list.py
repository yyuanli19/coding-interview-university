"""
Runtime: 856 ms, faster than 23.61% of Python3 online submissions for Palindrome Linked List.
Memory Usage: 74.3 MB, less than 5.12% of Python3 online submissions for Palindrome Linked List.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast != None:
            slow = slow.next
            
        left = head
        right = self.reverseList(slow)

        while right is not None:
            # print(left.val, right.val)
            if right.val != left.val:
                return False
            right = right.next
            left = left.next
        return True
        
        
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last
        
        
"""
recursive approach, using function stack to traverse the linked list from the back
Runtime: 1108 ms, faster than 5.06% of Python3 online submissions for Palindrome Linked List.
Memory Usage: 116.4 MB, less than 5.12% of Python3 online submissions for Palindrome Linked List.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.left = None
    def isPalindrome(self, head: ListNode) -> bool:
        self.left = head
        return self.traverse(head)
        
        
    def traverse(self, head: ListNode) -> ListNode:
        if head is None:
            return True
        res = self.traverse(head.next)
        res = res & (head.val == self.left.val)
        self.left = self.left.next
        return res
        

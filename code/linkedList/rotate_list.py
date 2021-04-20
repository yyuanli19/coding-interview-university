"""
Runtime: 36 ms, faster than 72.07% of Python3 online submissions for Rotate List.
Memory Usage: 14.2 MB, less than 60.94% of Python3 online submissions for Rotate List.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return
        # first walk over linked list to check for length
        length, tmp = 0, head
        while tmp:
            tmp = tmp.next
            length +=1
        # if equal to length no need to rotate
        if k%length == 0:
            return head
        # first find where to break
        slow, fast = head, head
        for _ in range((k%length)+1):
            fast = fast.next
        
        while fast is not None:
            slow = slow.next
            fast = fast.next

        new_head = slow.next
        slow.next = None
        slow = new_head
        while slow.next:
            # print(slow.val)
            slow = slow.next
        slow.next = head

        return new_head
            
            
        
"""
brilliant solution found in discussion
Runtime: 32 ms, faster than 90.68% of Python3 online submissions for Rotate List.
Memory Usage: 14.2 MB, less than 84.06% of Python3 online submissions for Rotate List.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return
        # first walk over linked list to check for length
        length, last = 1, head
        while last.next:
            last = last.next
            length +=1
        # if equal to length no need to rotate
        if k%length == 0:
            return head
        # first find where to break
        
        last.next = head
        for _ in range(length-(k%length)-1):
            head = head.next
            
        new_head = head.next
        head.next = None
        
        return new_head
    
            
            
        

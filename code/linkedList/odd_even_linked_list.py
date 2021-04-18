"""
two loops to find odd and even nodes respectively
Runtime: 52 ms, faster than 7.75% of Python3 online submissions for Odd Even Linked List.
Memory Usage: 17.4 MB, less than 6.38% of Python3 online submissions for Odd Even Linked List.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr = dummy
        old_node = head
        
        idx = 1
        while old_node is not None:
            if idx%2 != 0 :
                curr.next = ListNode(old_node.val)
                curr = curr.next
            old_node = old_node.next
            idx +=1
            
        idx = 1
        while head is not None:
            if idx%2 == 0 :
                curr.next = ListNode(head.val)
                curr = curr.next
            head = head.next
            idx +=1
        
        return dummy.next
            
"""
one loops to find odd and even nodes, but the space complexity is still the same
Runtime: 44 ms, faster than 56.14% of Python3 online submissions for Odd Even Linked List.
Memory Usage: 17.5 MB, less than 6.38% of Python3 online submissions for Odd Even Linked List.
"""
 
 # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        even = ListNode(0)
        odd = ListNode(0)
        dummy_odd = odd
        dummy_even = even
        old_node = head
        
        idx = 1
        while old_node is not None:
            if idx%2 != 0 :
                odd.next = ListNode(old_node.val)
                odd = odd.next
            else:
                even.next = ListNode(old_node.val)
                even = even.next
            old_node = old_node.next
            idx +=1
            
        odd.next = dummy_even.next
        return dummy_odd.next
        
"""
optimized version: one loops to find odd and even nodes, but not creating new nodes just point to head, then set the end of the linked list to point to None
Runtime: 44 ms, faster than 56.14% of Python3 online submissions for Odd Even Linked List.
Memory Usage: 16.5 MB, less than 15.91% of Python3 online submissions for Odd Even Linked List.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        even = ListNode(0)
        odd = ListNode(0)
        dummy_odd = odd
        dummy_even = even
        
        idx = 1
        while head is not None:
            if idx%2 != 0 :
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            head = head.next
            idx +=1
            
        even.next = None
        odd.next = dummy_even.next
        return dummy_odd.next
        
 """
 official solution using 3 pointer nodes
 Runtime: 44 ms, faster than 56.14% of Python3 online submissions for Odd Even Linked List.
Memory Usage: 16.2 MB, less than 84.90% of Python3 online submissions for Odd Even Linked List.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return
        odd, even = head, head.next
        evenHead = even

        while even is not None and even.next is not None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head
 

            
        

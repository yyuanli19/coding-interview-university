"""
    self solution + found solution
    Runtime: 72 ms, faster than 64.47% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
    Memory Usage: 16.6 MB, less than 24.93% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
        

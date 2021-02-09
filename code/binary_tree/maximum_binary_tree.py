"""
    Runtime: 224 ms, faster than 40.10% of Python3 online submissions for Maximum Binary Tree.
    Memory Usage: 14.9 MB, less than 67.13% of Python3 online submissions for Maximum Binary Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums)==0:
            return
        max_idx = self.find_max(nums)
        root = TreeNode(nums[max_idx])
        root.left = self.constructMaximumBinaryTree(nums[:max_idx])
        root.right = self.constructMaximumBinaryTree(nums[max_idx+1:])
        return root
    
    def find_max(self, nums):
        curr_max = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[curr_max]:
                curr_max = i
        return curr_max
        
"""
    excellent solution in discussion
    Runtime: 172 ms, faster than 99.64% of Python3 online submissions for Maximum Binary Tree.
    Memory Usage: 14.9 MB, less than 67.29% of Python3 online submissions for Maximum Binary Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        stack = []
        for x in nums:
            n = TreeNode(x)
            while stack and x > stack[-1].val:
                n.left = stack.pop()
            if stack:
                stack[-1].right = n
            stack.append(n)
            # print(x, stack[0])
        return stack[0]
        

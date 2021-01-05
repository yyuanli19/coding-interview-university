"""
    Runtime: 44 ms, faster than 91.28% of Python3 online submissions for Kth Smallest Element in a BST.
    Memory Usage: 18 MB, less than 69.43% of Python3 online submissions for Kth Smallest Element in a BST.
    THINK ABOUT RECURSIVE SOLUTION!
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root:
            return
        stack = [(root, False)]
        counter = 0
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    counter+=1
                    if counter == k:
                        return node.val
                else:
                    stack+= [(node.right, False), (node, True), (node.left, False)]
            
    
    

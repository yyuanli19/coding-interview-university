"""
    Runtime: 32 ms, faster than 68.75% of Python3 online submissions for Leaf-Similar Trees.
    Memory Usage: 14.1 MB, less than 83.93% of Python3 online submissions for Leaf-Similar Trees.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2:
            return True
        leaf1 = self.traversal(root1)
        leaf2 = self.traversal(root2)
        return leaf1==leaf2
    
    def traversal(self, root):
        if not root:
            return []
        stack, v = [root], []
        while stack:
            node = stack.pop()
            if node:
                if not node.left and not node.right:
                    v.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return v
        

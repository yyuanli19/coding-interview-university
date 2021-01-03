# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0
        stack = [(root, 1)]
        while stack:
            node, cur_d = stack.pop()
            if not node:
                return 0
            if cur_d > depth:
                depth = cur_d
            if node.right:
                stack.append((node.right,cur_d+1))
            if node.left:
                stack.append((node.left,cur_d+1))
        return depth

#with recursion
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))
        

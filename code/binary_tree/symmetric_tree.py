
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        stack = [root, root]
        while stack:
            left = stack.pop(0)
            right = stack.pop(0)
            if not left and not right: continue
            if not left or not right: return False
            if left.val != right.val: return False
            stack += [left.left, right.right, left.right, right.left]
        return True

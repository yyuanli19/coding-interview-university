"""
    needed the help of the solution
    Runtime: 240 ms, faster than 65.10% of Python3 online submissions for Subtree of Another Tree.
    Memory Usage: 15.5 MB, less than 21.46% of Python3 online submissions for Subtree of Another Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        return (not s is None) and (self.isIdentical(s, t) or
                                   self.isSubtree(s.left, t) or
                                   self.isSubtree(s.right, t))
        
    def isIdentical(self, s, t):
        if not s and not t:
            return True
        elif not s or not t:
            return False
        return s.val == t.val and self.isIdentical(s.left, t.left) and self.isIdentical(s.right, t.right)

        

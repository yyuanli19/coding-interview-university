"""
    recursion
    Runtime: 40 ms, faster than 39.55% of Python3 online submissions for Construct Binary Search Tree from Preorder Traversal.
    Memory Usage: 14.2 MB, less than 66.32% of Python3 online submissions for Construct Binary Search Tree from Preorder Traversal.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder)<1:
            return None
        if len(preorder)==1:
            return TreeNode(preorder[0])
        tree = TreeNode(preorder[0])
        index = None
        for i in range(len(preorder)):
            if preorder[i] > preorder[0]:
                index = i
                break
        if not index:
            index = len(preorder)
        tree.left = self.bstFromPreorder(preorder[1:index])
        tree.right = self.bstFromPreorder(preorder[index:])
        return tree
            
   
        

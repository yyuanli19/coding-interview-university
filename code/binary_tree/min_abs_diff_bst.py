"""
    make use of the property of binary search tree
    Runtime: 68 ms, faster than 10.86% of Python3 online submissions for Minimum Absolute Difference in BST.
    Memory Usage: 16.2 MB, less than 56.76% of Python3 online submissions for Minimum Absolute Difference in BST.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        par, min_diff = float("inf"), float("inf")
        stack, v = [(root, False)], []
        while stack:
            cur, visited = stack.pop()
            if cur:
                if visited:
                    min_diff = min(min_diff, abs(par-cur.val))
                    # print(par)
                    par = cur.val
                else:
                    stack += [(cur.right, False), (cur, True), (cur.left, False)]
        return min_diff
        
#TODO: think about the recursion way

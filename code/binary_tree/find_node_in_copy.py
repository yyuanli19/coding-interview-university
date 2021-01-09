"""
    recursion
    Runtime: 788 ms, faster than 6.01% of Python3 online submissions for Find a Corresponding Node of a Binary Tree in a Clone of That Tree.
    Memory Usage: 24.1 MB, less than 55.63% of Python3 online submissions for Find a Corresponding Node of a Binary Tree in a Clone of That Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not target:
            return None
        if not cloned:
            return None
        if cloned.val == target.val:
            return cloned
        cloned1 = self.getTargetCopy(original, cloned.left, target)
        cloned2 = self.getTargetCopy(original, cloned.right, target)
        return cloned1 if cloned1 else cloned2
        
"""
    iterative
    Runtime: 760 ms, faster than 7.56% of Python3 online submissions for Find a Corresponding Node of a Binary Tree in a Clone of That Tree.
    Memory Usage: 24.2 MB, less than 18.69% of Python3 online submissions for Find a Corresponding Node of a Binary Tree in a Clone of That Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not target:
            return None
        if not cloned:
            return None
        stack = [cloned]
        while stack:
            node = stack.pop()
            if node:
                if node.val == target.val:
                    return node
                stack += [node.right, node.left]
        

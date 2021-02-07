"""
    Runtime: 28 ms, faster than 84.05% of Python3 online submissions for Second Minimum Node In a Binary Tree.
    Memory Usage: 14 MB, less than 93.62% of Python3 online submissions for Second Minimum Node In a Binary Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        smallest = root.val
        if not root.left and not root.right:
            return -1
        stack, second_small = [root], float("inf")
        while stack:
            node = stack.pop()
            if node:
                if node.val < second_small and node.val != smallest:
                    second_small = node.val
                if node.left and node.right:
                    stack += [node.right, node.left]
        if second_small == float("inf"):
            return -1
        return second_small


"""
    small change from official solution
    Runtime: 20 ms, faster than 99.46% of Python3 online submissions for Second Minimum Node In a Binary Tree.
    Memory Usage: 14.3 MB, less than 16.89% of Python3 online submissions for Second Minimum Node In a Binary Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        smallest = root.val
        if not root.left and not root.right:
            return -1
        stack, second_small = [root], float("inf")
        while stack:
            node = stack.pop()
            if node:
                if node.val < second_small and node.val != smallest:
                    second_small = node.val
                if node.val == smallest:
                    if node.left and node.right:
                        stack += [node.right, node.left]
        if second_small == float("inf"):
            return -1
        return second_small 

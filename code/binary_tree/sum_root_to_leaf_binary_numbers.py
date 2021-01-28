"""
    iterative approach
    Runtime: 36 ms, faster than 75.24% of Python3 online submissions for Sum of Root To Leaf Binary Numbers.
    Memory Usage: 14.6 MB, less than 71.68% of Python3 online submissions for Sum of Root To Leaf Binary Numbers.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        res, stack = [], [(root, 0)]
        f_sum = 0
        while stack:
            node, curr = stack.pop()
            if node:
                curr = (curr << 1) | node.val
                if node.right:
                    stack.append((node.right, curr))
                if node.left:
                    stack.append((node.left, curr))
                if not node.right and not node.left:
                    res.append(curr)
                    f_sum += curr
             
        return f_sum
        
        
"""
    recursive solution, needed a lot of help from the solution
    Runtime: 32 ms, faster than 92.23% of Python3 online submissions for Sum of Root To Leaf Binary Numbers.
    Memory Usage: 14.4 MB, less than 91.34% of Python3 online submissions for Sum of Root To Leaf Binary Numbers.

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        f_sum = self.recur(root, 0)
        return f_sum
    
    def recur(self, root, curr_sum):
        if not root:
            return 0
        curr_sum = (curr_sum << 1) | root.val
        if not root.left and not root.right:
            return curr_sum
        # if root.left:
        #     curr_sum += self.recur(root.left, curr_sum)
        # if root.right:
        #     curr_sum += self.recur(root.right, curr_sum)
        return self.recur(root.left, curr_sum)+self.recur(root.right, curr_sum)

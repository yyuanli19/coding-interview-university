"""
    Runtime: 60 ms, faster than 5.34% of Python3 online submissions for Sum of Left Leaves.
    Memory Usage: 14.7 MB, less than 82.00% of Python3 online submissions for Sum of Left Leaves.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        stack, left_sum = [(root,"root")], 0
        while stack:
            node, side = stack.pop()
            if node:
                if not node.left and not node.right:
                    if side == "left":
                        left_sum += node.val
                if node.left:
                    stack.append((node.left, "left"))
                if node.right:
                    stack.append((node.right, "right"))
        return left_sum
        
"""
    Runtime: 40 ms, faster than 12.14% of Python3 online submissions for Sum of Left Leaves.
    Memory Usage: 15.1 MB, less than 25.88% of Python3 online submissions for Sum of Left Leaves.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        return self.recur(root, 0)
    
    def recur(self, root, left_sum):
        if not root:
            return 0
        # print(root.val)
        if root.left and not root.left.left and not root.left.right:
            # print("true")
            return left_sum + root.left.val + self.recur(root.right, left_sum)
        return self.recur(root.left, left_sum) + self.recur(root.right, left_sum)
        

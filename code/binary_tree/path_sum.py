# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# bfs with a queque
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        stack = [(root, sum-root.val)]
        while stack:
            node, curr_left = stack.pop(0)
            if node.left:
                stack.append((node.left, curr_left-node.left.val))
            if node.right:
                stack.append((node.right, curr_left-node.right.val))
            if not node.left and not node.right and curr_left==0:
                return True
        return False

# dfs with a queque, can also use the sum instead of the minus
# can do preorder instead of postorder first, but will be slower
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        stack = [(root, sum-root.val)]
        while stack:
            node, curr_left = stack.pop()
            
            if node.right:
                stack.append((node.right, curr_left-node.right.val))
            if node.left:
                stack.append((node.left, curr_left-node.left.val))
            if not node.left and not node.right and curr_left==0:
                return True
        return False

#recursion
class Solution:
   def hasPathSum(self, root: TreeNode, sum: int) -> bool:
       if not root:
           return False
       if not root.left and not root.right and sum == root.val:
           return True
       return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)


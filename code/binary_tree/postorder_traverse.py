# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack, v = [root], []
        while stack:
            node = stack.pop()
            if node:
                v.append(node.val)
                stack += [node.left, node.right]
        return v[::-1]



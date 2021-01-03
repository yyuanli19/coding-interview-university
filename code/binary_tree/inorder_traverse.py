# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# iteratively with a stack
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack, v = [(root, False)], []
        while stack:
            cur, visited = stack.pop()
            if cur:
                if visited:
                    v.append(cur.val)
                else:
                    stack += [(cur.right, False), (cur, True), (cur.left, False)]
            
        return v

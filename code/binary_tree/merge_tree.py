"""
    self solution, not sure how it worked out exactly
    Runtime: 100 ms, faster than 19.08% of Python3 online submissions for Merge Two Binary Trees.
    Memory Usage: 15.7 MB, less than 15.28% of Python3 online submissions for Merge Two Binary Trees.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return None
        if t1 and not t2:
            #print('t1', t1)
            root = TreeNode(t1.val)
            root.left = self.mergeTrees(t1.left, None)
            root.right = self.mergeTrees(t1.right, None)
        elif not t1 and t2:
            #print('t2', t2)
            root = TreeNode(t2.val)
            root.left = self.mergeTrees(None, t2.left)
            root.right = self.mergeTrees(None, t2.right)
        else:
            root = TreeNode(t1.val + t2.val)
            root.left = self.mergeTrees(t1.left, t2.left)
            root.right = self.mergeTrees(t1.right, t2.right)
        return root
        
"""
    adaptation based on official solution
    Runtime: 84 ms, faster than 87.85% of Python3 online submissions for Merge Two Binary Trees.
    Memory Usage: 15.8 MB, less than 15.28% of Python3 online submissions for Merge Two Binary Trees.
"""
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return None
        if not t1:
            return t2
        if not t2:
            return t1
        root = TreeNode(t1.val+t2.val)
        root.left = self.mergeTrees(t1.left, t2.left)
        root.right = self.mergeTrees(t1.right, t2.right)
        return root

"""
    offical iterative solution
    Runtime: 88 ms, faster than 70.05% of Python3 online submissions for Merge Two Binary Trees.
    Memory Usage: 15.3 MB, less than 85.98% of Python3 online submissions for Merge Two Binary Trees.
"""
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        
        stack = [(t1, t2)]
        while stack:
            node1, node2 = stack.pop()
            if not node2:
                continue
            node1.val += node2.val
            if node1.left:
                stack += [(node1.left, node2.left)]
            else:
                node1.left = node2.left
            if node1.right:
                stack += [(node1.right, node2.right)]
            else:
                node1.right = node2.right
        return t1
            

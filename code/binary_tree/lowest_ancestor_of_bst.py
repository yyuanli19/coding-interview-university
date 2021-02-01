"""
    Runtime: 88 ms, faster than 26.32% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
    Memory Usage: 18.4 MB, less than 32.23% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_path = self.find_path(root, p, [])
        q_path = self.find_path(root, q, [])

        for i in range(min(len(p_path), len(q_path))):
            if p_path[i] != q_path[i]:
                return TreeNode(p_path[i-1])

        return TreeNode(p_path[min(len(p_path), len(q_path))-1])
        
        
    def find_path(self, root, node, res):
        if root:
            res.append(root.val)
            if root.val == node.val:
                return res
            if root.val > node.val:
                self.find_path(root.left, node, res)
            if root.val < node.val:
                self.find_path(root.right, node, res)
        return res
        
"""
    offcial recursive amazing solution
    Runtime: 84 ms, faster than 31.33% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
    Memory Usage: 18.4 MB, less than 32.23% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
            
            
"""
    offcial iterative amazing solution
    Runtime: 144 ms, faster than 5.31% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
    Memory Usage: 18.2 MB, less than 91.65% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
                return root

"""
    Runtime: 36 ms, faster than 22.13% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.
    Memory Usage: 14.4 MB, less than 33.47% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        sorted_node = self.inorder(root, [])
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                index = self.find_index(sorted_node, node.val)
                node.val = sum(sorted_node[index:])
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return root
        
    
    def find_index(self, vals, target):
        for i in range(len(vals)):
            if vals[i] == target:
                return i
            
        
    def inorder(self, root, res):
        if root:
            if root.left:
                self.inorder(root.left, res)
            res.append(root.val)
            if root.right:
                self.inorder(root.right, res)
        return res

"""
    recursive version of the same code
    Runtime: 32 ms, faster than 67.49% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.
    Memory Usage: 14.5 MB, less than 33.47% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        sorted_node = self.inorder(root, [])
        return self.revise_tree(root, sorted_node)
        
    def revise_tree(self, root, nodelist):
        if root:
            index = self.find_index(nodelist, root.val)
            root.val = sum(nodelist[index:])
            if root.left:
                self.revise_tree(root.left, nodelist)
            if root.right:
                self.revise_tree(root.right, nodelist)
        return root
        
    def find_index(self, vals, target):
        for i in range(len(vals)):
            if vals[i] == target:
                return i
            
        
    def inorder(self, root, res):
        if root:
            if root.left:
                self.inorder(root.left, res)
            res.append(root.val)
            if root.right:
                self.inorder(root.right, res)
        return res

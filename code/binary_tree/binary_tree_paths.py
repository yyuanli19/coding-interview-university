"""
    iterative
    Runtime: 36 ms, faster than 40.91% of Python3 online submissions for Binary Tree Paths.
    Memory Usage: 14.3 MB, less than 62.36% of Python3 online submissions for Binary Tree Paths.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        stack = [(root, "")]
        res = []
        while stack:
            node, char = stack.pop()
            if node:
                # print(node.val, char)
                char += str(node.val)
                if not node.left and not node.right:
                    res.append(char)
                char += "->"
                if node.right:
                    stack.append((node.right, char))
                if node.left:
                    stack.append((node.left, char))
        return res
    
"""
    recursive
    Runtime: 40 ms, faster than 13.65% of Python3 online submissions for Binary Tree Paths.
    Memory Usage: 14.2 MB, less than 85.94% of Python3 online submissions for Binary Tree Paths.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res = self.recur(root, "", [])
        return res
    
    def recur(self, root, char, res):
        if not root:
            return []
        char += str(root.val)
        if not root.left and not root.right:
            res.append(char)
            # this line is actually not needed
            char = ""
        char += "->"
        self.recur(root.left, char, res)
        self.recur(root.right, char, res)
        return res
        

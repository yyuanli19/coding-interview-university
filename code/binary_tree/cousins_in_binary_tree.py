"""
    bfs
    Runtime: 40 ms, faster than 13.00% of Python3 online submissions for Cousins in Binary Tree.
    Memory Usage: 14.4 MB, less than 42.25% of Python3 online submissions for Cousins in Binary Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return True
        queque = [(root, 0)]
        cousin = []
        while queque:
            temp = []
            while queque:
                node, parent = queque.pop(0)
                if node:
                    if node.val in (x,y):
                        cousin.append(parent)
                    if node.left:
                        temp.append((node.left, node.val))
                    if node.right:
                        temp.append((node.right, node.val))
            queque = temp
            if len(cousin)==1:
                return False
            if len(cousin)==2 and cousin[0]!=cousin[1]:
                return True
        return False
                
    
"""
    dfs recursion found in discussion
    Runtime: 28 ms, faster than 89.30% of Python3 online submissions for Cousins in Binary Tree.
    Memory Usage: 14.3 MB, less than 42.25% of Python3 online submissions for Cousins in Binary Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return True
        res = self.dfs(root, x, y, root, 0, [])
        return res[0][0] == res[1][0] and res[0][1] != res[1][1]
    
    def dfs(self, root, x, y, parent, depth, res):
        if not root:
            return
        if len(res) == 2:
            return res
        if root.val in (x,y):
            res.append((depth, parent))
        self.dfs(root.left, x, y,  root.val, depth+1, res)
        self.dfs(root.right, x, y,  root.val, depth+1, res)
        return res
            
        

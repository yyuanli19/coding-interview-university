"""
    Runtime: 36 ms, faster than 37.92% of Python3 online submissions for Binary Tree Right Side View.
    Memory Usage: 14 MB, less than 99.38% of Python3 online submissions for Binary Tree Right Side View.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        leaf = self.levelOrder(root)
        res = []
        for row in leaf.keys():
            res.append(leaf[row][-1])
        return res
    
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        enqueque = deque([(0, root)])
        v = {}
        while enqueque:
            row, node = enqueque.popleft()
            if node:
                v[row] = v.get(row, []) + [node.val]
                enqueque += (row+1, node.left), (row+1, node.right)
        return v
        
"""
    improved level order traversal
    Runtime: 28 ms, faster than 89.66% of Python3 online submissions for Binary Tree Right Side View.
    Memory Usage: 14.2 MB, less than 80.32% of Python3 online submissions for Binary Tree Right Side View.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        return self.levelOrder(root)
    
    def levelOrder(self, root):
        enqueque = deque([(0, root)])
        res, level = [], -1
        while enqueque:
            row, node = enqueque.popleft()
            if node:
                if row > level:
                    res.append(node.val)
                    level = row
                enqueque += (row+1, node.right), (row+1, node.left)
        return res
        
        
"""
    found recursive solution
    Runtime: 36 ms, faster than 37.72% of Python3 online submissions for Binary Tree Right Side View.
    Memory Usage: 14.3 MB, less than 54.04% of Python3 online submissions for Binary Tree Right Side View.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        return self.recur(root, 0, [])
    
    def recur(self, root, depth, res):
        if not root:
            return
        if depth == len(res):
            res.append(root.val)
        self.recur(root.right, depth+1, res)
        self.recur(root.left, depth+1, res)
        return res
        



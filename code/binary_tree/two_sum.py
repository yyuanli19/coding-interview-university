"""
    Runtime: 80 ms, faster than 71.87% of Python3 online submissions for Two Sum IV - Input is a BST.
    Memory Usage: 17.5 MB, less than 65.03% of Python3 online submissions for Two Sum IV - Input is a BST.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return None
        return self.preorder(root, k, set())
    
    def preorder(self, root, k, res):
        if not root:
            return False
        # print(res, root.val)
        if root.val in res:
            return True
        res.add(k-root.val)
        return self.preorder(root.left, k, res) or self.preorder(root.right, k, res)
                
        
"""
    level order traversal
    Runtime: 124 ms, faster than 18.57% of Python3 online submissions for Two Sum IV - Input is a BST.
    Memory Usage: 16.4 MB, less than 89.29% of Python3 online submissions for Two Sum IV - Input is a BST.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return None
        queque, dic = [root], set()
        while queque:
            node = queque.pop(0)
            if node:
                if node.val in dic:
                    return True
                dic.add(k-node.val)
                if node.left:
                    queque.append(node.left)
                if node.right:
                    queque.append(node.right)
        return False

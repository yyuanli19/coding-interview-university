"""
    Runtime: 92 ms, faster than 94.79% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.
    Memory Usage: 17.8 MB, less than 46.03% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        nodesum = 0
        enqueque = [(None, None, root)]
        while enqueque:
            tmp = []
            while enqueque:
                grandparent, parent, node = enqueque.pop(0)
                if node:
                    if grandparent and grandparent%2 == 0:
                        nodesum += node.val
                    if node.left:
                        tmp += [(parent, node.val, node.left)]
                    if node.right:
                        tmp += [(parent, node.val, node.right)]
            enqueque = tmp
            
        return nodesum
       
"""
    solution from discussion
    Runtime: 100 ms, faster than 68.88% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.
    Memory Usage: 17.7 MB, less than 77.42% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        return self.recur(root, 1, 1)
    
    def recur(self, root, parent, grandparent):
        if not root:
            return 0
        return self.recur(root.left, root.val, parent) + self.recur(root.right, root.val, parent) + root.val*(1 - grandparent % 2)
            
 

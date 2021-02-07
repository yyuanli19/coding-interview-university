"""
    Runtime: 48 ms, faster than 94.80% of Python3 online submissions for Find Mode in Binary Search Tree.
    Memory Usage: 18.4 MB, less than 69.33% of Python3 online submissions for Find Mode in Binary Search Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        stack, count = [root], {}
        cur_max = 0
        while stack:
            node = stack.pop()
            if node:
                count[node.val] = count.get(node.val, 0) +1
                cur_max = max(cur_max, count[node.val])
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        res = []
        for key, val in count.items():
            if val == cur_max:
                res.append(key)
        return res
                    
        

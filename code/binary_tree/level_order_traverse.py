# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        enqueque = deque([(0, root)])
        v = {}
        while enqueque:
            row, node = enqueque.popleft()
            if node:
                v[row] = v.get(row, []) + [node.val]
                enqueque += (row+1, node.left), (row+1, node.right)
        return [v[row] for row in sorted(v.keys())]
        
        

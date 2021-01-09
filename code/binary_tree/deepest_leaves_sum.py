"""
    bfs solution
    Runtime: 188 ms, faster than 5.10% of Python3 online submissions for Deepest Leaves Sum.
    Memory Usage: 17.8 MB, less than 33.06% of Python3 online submissions for Deepest Leaves Sum.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        enqueque = deque([(0, root)])
        v = {}
        while enqueque:
            row, node = enqueque.popleft()
            if node:
                v[row] = v.get(row, []) + [node.val]
                enqueque += (row+1, node.left), (row+1, node.right)
        return sum(v[max(v.keys())])
        


"""
    Runtime: 208 ms, faster than 69.69% of Python3 online submissions for Range Sum of BST.
    Memory Usage: 22.2 MB, less than 34.84% of Python3 online submissions for Range Sum of BST.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return None
        stack = [root]
        curr_sum = 0
        while stack:
            node = stack.pop()
            if node:
                if node.val > high:
                    stack.append(node.left)
                elif node.val < low:
                    stack.append(node.right)
                else:
                    curr_sum += node.val
                    stack += [node.right, node.left]
        return curr_sum
        
"""
    adapted recursive solution based on official solution
    Runtime: 208 ms, faster than 69.69% of Python3 online submissions for Range Sum of BST.
    Memory Usage: 22.3 MB, less than 34.84% of Python3 online submissions for Range Sum of BST.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return None
        
        c = self.dfs(root, low, high, [])
        return sum(c)
        
    def dfs(self, root, low, high, ans):
        if root:
            if root.val > high:
                self.dfs(root.left, low, high, ans)
            if root.val < low:
                self.dfs(root.right, low, high, ans)
            if low <= root.val <= high:
                ans.append(root.val)
                self.dfs(root.left, low, high, ans)
                self.dfs(root.right, low, high, ans)
        return ans
    

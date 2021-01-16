"""
    Runtime: 44 ms, faster than 14.55% of Python3 online submissions for Increasing Order Search Tree.
    Memory Usage: 14.4 MB, less than 37.72% of Python3 online submissions for Increasing Order Search Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        ordered = self.inorder(root, [])
        # print(ordered)
        root = TreeNode(ordered[0])
        node = root
        for i in ordered[1:]:
            node.right = TreeNode(i)
            node = node.right
            # print(root)
        return root
    
    def inorder(self, root, res):
        if not root:
            return res
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)
        return res


"""
    official solution
"""
class Solution:
    def increasingBST(self, root):
        def inorder(node):
            if node:
                inorder(node.left)
                node.left = None
                self.cur.right = node
                self.cur = node
                inorder(node.right)

        ans = self.cur = TreeNode(None)
        inorder(root)
        return ans.right

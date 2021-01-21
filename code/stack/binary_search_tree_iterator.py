"""
    Runtime: 68 ms, faster than 91.04" of Python3 online submissions for Binary Search Tree Iterator.
    Memory Usage: 20.1 MB, less than 90.33% of Python3 online submissions for Binary Search Tree Iterator.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.inorder = self.traverse(root, [])
        

    def next(self) -> int:
        return self.inorder.pop(0)

    def hasNext(self) -> bool:
        if len(self.inorder) != 0:
            return True
        return False
        
    def traverse(self, root, res):
        if not root:
            return
        if root.left:
            self.traverse(root.left, res)
        res.append(root.val)
        if root.right:
            self.traverse(root.right, res)
        return res
            
                
        
"""
    neat official solution
    Runtime: 76 ms, faster than 54.42% of Python3 online submissions for Binary Search Tree Iterator.
    Memory Usage: 20.6 MB, less than 59.59% of Python3 online submissions for Binary Search Tree Iterator.
"""
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.inorder = []
        self.traverse_left(root)
        
    def next(self) -> int:
        node = self.inorder.pop()
        if node.right:
            self.traverse_left(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.inorder) > 0
        
    def traverse_left(self, root):
        while root:
            self.inorder.append(root)
            root = root.left

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

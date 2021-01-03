"""
    iterative with a stack
"""
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack, v = [root], []
        while stack:
            node = stack.pop()
            if node:
                v.append(node.val)
                stack += [node.right, node.left]
        return v

#todo: think about recursive way

"""
    recursive
    Runtime: 52 ms, faster than 57.57% of Python3 online submissions for N-ary Tree Postorder Traversal.
    Memory Usage: 16 MB, less than 74.91% of Python3 online submissions for N-ary Tree Postorder Traversal.
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return None
        return self.dfs(root, [])
        
    def dfs(self, root, v):
        if not root:
            return None
        for i in root.children:
            self.dfs(i, v)
        v.append(root.val)
        return v
        
"""
    iterative 1
    Runtime: 56 ms, faster than 25.32% of Python3 online submissions for N-ary Tree Postorder Traversal.
    Memory Usage: 16.1 MB, less than 23.63% of Python3 online submissions for N-ary Tree Postorder Traversal.
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return None
        stack, v = [(root, False)], []
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    v.append(node.val)
                else:
                    stack.append((node, True))
                    for i in node.children[::-1]:
                        stack.append((i, False))
                    
        return v
        
   

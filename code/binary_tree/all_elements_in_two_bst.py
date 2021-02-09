"""
    Runtime: 344 ms, faster than 62.36% of Python3 online submissions for All Elements in Two Binary Search Trees.
    Memory Usage: 21.6 MB, less than 61.24% of Python3 online submissions for All Elements in Two Binary Search Trees.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        list1 = self.inorder(root1, [])
        list2 = self.inorder(root2, [])
        start1, start2 = 0, 0
        sorted_list =[]
        while start1<len(list1) and start2<len(list2):
            if list1[start1] < list2[start2]:
                sorted_list.append(list1[start1])
                start1 += 1
            elif list1[start1] > list2[start2]:
                sorted_list.append(list2[start2])
                start2 += 1
            else:
                sorted_list += [list1[start1], list2[start2]]
                start1 += 1
                start2 += 1
        if start1<len(list1):
            sorted_list += list1[start1:]
        if start2<len(list2):
            sorted_list += list2[start2:]
        return sorted_list
        
    def inorder(self, root, res):
        if root:
            if root.left:
                self.inorder(root.left, res)
            res.append(root.val)
            if root.right:
                self.inorder(root.right, res)
        return res

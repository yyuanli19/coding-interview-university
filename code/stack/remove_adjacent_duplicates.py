"""
    Runtime: 68 ms, faster than 76.38% of Python3 online submissions for Remove All Adjacent Duplicates In String.
    Memory Usage: 14.9 MB, less than 21.15% of Python3 online submissions for Remove All Adjacent Duplicates In String.
"""
class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for i in S:
            if stack and i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)
        

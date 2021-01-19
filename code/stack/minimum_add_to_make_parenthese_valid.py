"""
    Runtime: 32 ms, faster than 63.86% of Python3 online submissions for Minimum Add to Make Parentheses Valid.
    Memory Usage: 14.4 MB, less than 14.64% of Python3 online submissions for Minimum Add to Make Parentheses Valid.
"""
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = []
        rest = 0
        for i in S:
            if i ==")":
                if stack:
                    stack.pop()
                else:
                    rest+=1
            else:
                stack.append(i)
        return len(stack) + rest
        

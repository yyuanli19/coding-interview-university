"""
    Runtime: 32 ms, faster than 88.14% of Python3 online submissions for Make The String Great.
    Memory Usage: 14 MB, less than 92.84% of Python3 online submissions for Make The String Great.
"""
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in s:
            if stack and abs(ord(i) - ord(stack[-1]))==32:
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)
            

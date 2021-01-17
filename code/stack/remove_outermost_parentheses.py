"""
    Runtime: 44 ms, faster than 28.57% of Python3 online submissions for Remove Outermost Parentheses.
    Memory Usage: 14.4 MB, less than 38.33% of Python3 online submissions for Remove Outermost Parentheses.
"""
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        start, left = 0, 0
        s = ""
        for i in range(len(S)):
            if S[i] == "(":
                left += 1
            else:
                left -=1
            if left==0:
                s += S[start+1:i]
                start, left = i+1, 0
        return s
                
        

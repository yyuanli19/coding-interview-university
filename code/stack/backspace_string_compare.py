"""
    Runtime: 32 ms, faster than 61.98% of Python3 online submissions for Backspace String Compare.
    Memory Usage: 14.4 MB, less than 22.78% of Python3 online submissions for Backspace String Compare.
"""class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        S_back = self.stackString(S)
        T_back = self.stackString(T)
        return S_back == T_back
        
    def stackString(self, string):
        stack = []
        for i in string:
            if stack and i=="#":
                stack.pop()
            #be careful with the case where everything has been deleted
            elif i!= "#":
                stack.append(i)
        return "".join(stack)
            
        

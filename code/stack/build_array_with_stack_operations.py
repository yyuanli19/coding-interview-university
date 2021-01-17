"""
    Runtime: 44 ms, faster than 12.77% of Python3 online submissions for Build an Array With Stack Operations.
    Memory Usage: 14 MB, less than 93.36% of Python3 online submissions for Build an Array With Stack Operations.
"""
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        ops = []
        for i in range(1, n+1):
            if stack == target:
                return ops
            if stack and stack[-1] not in target:
                stack.pop()
                ops.append("Pop")
            stack.append(i)
            ops.append("Push")
            # print(stack, ops)
        return ops
     
"""
    came up after read discussion
    Runtime: 28 ms, faster than 90.60% of Python3 online submissions for Build an Array With Stack Operations.
    Memory Usage: 14.2 MB, less than 52.20% of Python3 online submissions for Build an Array With Stack Operations.
"""
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ops = []
        for i in range(1, target[-1]+1):
            ops.append("Push")
            if i not in target:
                ops.append("Pop")
        return ops
            
                
        
                
        

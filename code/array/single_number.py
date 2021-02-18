"""
    Runtime: 136 ms, faster than 57.62% of Python3 online submissions for Single Number.
    Memory Usage: 16.6 MB, less than 63.50% of Python3 online submissions for Single Number.
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        appeared = {}
        for i in nums:
            appeared[i] = appeared.get(i, 0) +1
            
        for key, val in appeared.items():
            if val == 1:
                return key
    

"""
    Runtime: 32 ms, faster than 62.82% of Python3 online submissions for Plus One.
    Memory Usage: 14.3 MB, less than 7.54% of Python3 online submissions for Plus One.
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #print("passed in: ", digits)
        if digits == [9]:
            return [1, 0]
        digits[-1] += 1
        #print("add one: ", digits)
        if digits[-1] == 10:
            digits[-1] = 0
            digits = self.plusOne(digits[:-1]) + [digits[-1]]
        return digits


    

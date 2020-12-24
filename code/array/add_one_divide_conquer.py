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

"""
    found very interesting solution
    Runtime: 28 ms, faster than 86.54% of Python3 online submissions for Plus One.
    Memory Usage: 14 MB, less than 85.15% of Python3 online submissions for Plus One.
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)):
            if digits[~i] < 9:
                digits[~i] += 1
                return digits
            digits[~i] = 0
        return [1] + [0] * len(digits)


        

    

"""
    Runtime: 116 ms, faster than 71.68% of Python3 online submissions for Contains Duplicate.
    Memory Usage: 21.5 MB, less than 5.11% of Python3 online submissions for Contains Duplicate.
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for i in nums:
            if i in dic:
                return True
            else:
                dic[i] = 1
        return False
        
        


"""
    Runtime: 48 ms, faster than 69.56% of Python3 online submissions for Search Insert Position.
    Memory Usage: 15.1 MB, less than 12.54% of Python3 online submissions for Search Insert Position.
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        s = 0
        while s < len(nums):
            if nums[s]<target:
                s +=1
            else: break
        return s
    

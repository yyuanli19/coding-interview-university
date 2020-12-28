"""
    Runtime: 52 ms, faster than 65.14% of Python3 online submissions for Third Maximum Number.
    Memory Usage: 15.3 MB, less than 62.55% of Python3 online submissions for Third Maximum Number.
"""
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        nums = sorted(nums, reverse=True)
        goal = 2
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                goal += 1
            elif i == goal:
                return nums[i]
        return nums[0]
            

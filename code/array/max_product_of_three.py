"""
    Runtime: 256 ms, faster than 46.45% of Python3 online submissions for Maximum Product of Three Numbers.
    Memory Usage: 15.4 MB, less than 48.24% of Python3 online submissions for Maximum Product of Three Numbers.
"""
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return max(nums[-1]*nums[-2]*nums[-3], nums[-1]*nums[1]*nums[0])
        

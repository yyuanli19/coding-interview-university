"""
    personal solution
    Runtime: 2400 ms, faster than 9.98% of Python3 online submissions for Missing Number.
    Memory Usage: 15.4 MB, less than 54.39% of Python3 online submissions for Missing Number.
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        for i in range(len(nums)+1):
            if i not in nums:
                return i
        
"""
    official xor solution
    Runtime: 128 ms, faster than 71.79% of Python3 online submissions for Missing Number.
    Memory Usage: 15.5 MB, less than 15.38% of Python3 online submissions for Missing Number.
"""
class Solution:
    def missingNumber(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing

"""
    found sum solution
    Runtime: 128 ms, faster than 71.79% of Python3 online submissions for Missing Number.
    Memory Usage: 15.2 MB, less than 67.94% of Python3 online submissions for Missing Number.
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        for i in range(len(nums)):
            missing += i - nums[i]
        
        return missing

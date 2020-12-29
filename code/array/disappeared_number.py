"""
    Runtime: 324 ms, faster than 91.80% of Python3 online submissions for Find All Numbers Disappeared in an Array.
    Memory Usage: 23.6 MB, less than 33.25% of Python3 online submissions for Find All Numbers Disappeared in an Array.
"""
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        new_nums = set(nums)
        missing = []
        for i in range(1, len(nums)+1):
            if not i in new_nums:
                missing += i,
        return missing
        

"""
    found solution that flips the sign of the numbers
    Runtime: 364 ms, faster than 49.70% of Python3 online submissions for Find All Numbers Disappeared in an Array.
    Memory Usage: 21.7 MB, less than 94.13% of Python3 online submissions for Find All Numbers Disappeared in an Array.
"""
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
        

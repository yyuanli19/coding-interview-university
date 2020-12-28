"""
    Runtime: 52 ms, faster than 46.25% of Python3 online submissions for Move Zeroes.
    Memory Usage: 15.5 MB, less than 12.78% of Python3 online submissions for Move Zeroes.
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            if nums[0] == 0:
                return []
            else:
                return nums
        c, n = 0, 1
        while n < len(nums):
            if nums[c] == 0:
                if nums[n] != 0:
                    nums[c] = nums[n]
                    nums[n] = 0
                    c+=1
            else:
                c+=1
            n+=1
                    
        

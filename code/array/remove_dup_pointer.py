"""
    Runtime: 84 ms, faster than 55.83% of Python3 online submissions for Remove Duplicates from Sorted Array.
    Memory Usage: 15.8 MB, less than 62.18% of Python3 online submissions for Remove Duplicates from Sorted Array.
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start = 0
        c = 1
            
        while c < len(nums):
            if nums[c] != nums[start]:
                nums[start+1] = nums[c]
                start += 1
            c += 1
        return len(nums[:start+1])

"""
    Runtime: 92 ms, faster than 55.07% of Python3 online submissions for Contains Duplicate II.
    Memory Usage: 21.7 MB, less than 30.01% of Python3 online submissions for Contains Duplicate II.
"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic and i - dic[nums[i]] <=k:
                return True
            else:
                dic[nums[i]] = i
        return False
        

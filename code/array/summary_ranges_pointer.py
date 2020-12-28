"""
    found solution
    Runtime: 24 ms, faster than 90.51% of Python3 online submissions for Summary Ranges.
    Memory Usage: 14 MB, less than 76.47% of Python3 online submissions for Summary Ranges.
"""
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i, result, N = 0, [], len(nums)
        
        while i < N:
            beg = end = i
            while end < N - 1 and nums[end] + 1 == nums[end + 1]: end += 1
            result.append(str(nums[beg]) + ("->" + str(nums[end])) *(beg != end))
            i = end + 1
        
        return result
        

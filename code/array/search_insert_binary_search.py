"""
found binary search solution
Runtime: 44 ms, faster than 89.37% of Python3 online submissions for Search Insert Position.
Memory Usage: 15.1 MB, less than 12.54% of Python3 online submissions for Search Insert Position.
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l , r = 0, len(nums)-1
        while l <= r:
            mid=(l+r)//2
            if nums[mid]== target:
                return mid
            if nums[mid] < target:
                l = mid+1
            else:
                r = mid-1
        return l


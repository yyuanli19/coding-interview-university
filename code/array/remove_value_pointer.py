
"""
Runtime: 28 ms, faster than 90.25% of Python3 online submissions for Remove Element.
Memory Usage: 14.3 MB, less than 8.61% of Python3 online submissions for Remove Element.
"""
    
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start, end = 0, len(nums)-1
        while start <= end:
            if nums[start] != val:
                start += 1
            else:
                if nums[end] != val:
                    nums[start] = nums[end]
                end -= 1
        return start

"""
previous solution
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start, end = 0, len(nums) -1;
        while start<=end:
            if nums[start] == val:
                nums[start] = nums[end]
                end -= 1
            else: start += 1
        return start

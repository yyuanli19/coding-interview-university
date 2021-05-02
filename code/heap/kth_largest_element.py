"""
Runtime: 52 ms, faster than 98.84% of Python3 online submissions for Kth Largest Element in an Array.
Memory Usage: 15.1 MB, less than 42.75% of Python3 online submissions for Kth Largest Element in an Array.
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-1*num for num in nums]
        heapq.heapify(nums)
        for i in range(k-1):
            heapq.heappop(nums)
            
        return -1*heapq.heappop(nums)
        

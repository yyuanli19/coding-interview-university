"""
Runtime: 192 ms, faster than 59.36% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
Memory Usage: 19.9 MB, less than 94.02% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
"""
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        gen = heapq.merge(*matrix)
        for i in range(k-1):
            next(gen)
        return next(gen)



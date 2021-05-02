"""
Runtime: 32 ms, faster than 61.53% of Python3 online submissions for Last Stone Weight.
Memory Usage: 14.3 MB, less than 50.94% of Python3 online submissions for Last Stone Weight.
"""
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 2:
            return abs(stones[0] - stones[1])
        heap = []
        for i in stones:
            heapq.heappush(heap, -1*i)
        # print(heap)
        while len(heap) >= 2:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            if abs(x-y) != 0:
                heapq.heappush(heap, -1*abs(x-y))
            # print(heap)
        if heap:
            return -1*heap[0]
        return 0
        
"""
use list comprehession and heapify speeded up the script
Runtime: 28 ms, faster than 84.38% of Python3 online submissions for Last Stone Weight.
Memory Usage: 14.3 MB, less than 17.38% of Python3 online submissions for Last Stone Weight.
"""
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 2:
            return abs(stones[0] - stones[1])
        heap = [-1*x for x in stones]
        heapq.heapify(heap)
        # print(heap)
        while len(heap) >= 2:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            # abs() is also not needed since we know the first popped is smaller than the
            # second poped, we can control the sign
            if x-y != 0:
                heapq.heappush(heap, x-y)
            # print(heap)
        if heap:
            return -1*heap[0]
        return 0
        
"""
drop the if check and just insert it back speeded up again
Runtime: 24 ms, faster than 95.53% of Python3 online submissions for Last Stone Weight.
Memory Usage: 14.3 MB, less than 17.38% of Python3 online submissions for Last Stone Weight.
"""
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 2:
            return abs(stones[0] - stones[1])
        heap = [-1*x for x in stones]
        heapq.heapify(heap)
        # print(heap)
        while len(heap) >= 2 and heap[0] != 0:
            heapq.heappush(heap, heapq.heappop(heap) - heapq.heappop(heap))
            
        return -1*heap[0]
        

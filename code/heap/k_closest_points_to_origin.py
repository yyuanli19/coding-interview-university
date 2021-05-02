"""
Runtime: 712 ms, faster than 33.93% of Python3 online submissions for K Closest Points to Origin.
Memory Usage: 19.9 MB, less than 59.50% of Python3 online submissions for K Closest Points to Origin.
"""
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k == len(points):
            return points
        heap =  []
        for i, point in enumerate(points):
            dist = math.sqrt(point[0]**2 + point[1]**2)
            heapq.heappush(heap, (dist, point))
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans
            
            
"""
max-heap solution
Runtime: 688 ms, faster than 49.89% of Python3 online submissions for K Closest Points to Origin.
Memory Usage: 20 MB, less than 36.03% of Python3 online submissions for K Closest Points to Origin.
"""
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k == len(points):
            return points
        heap =  []
        for i, point in enumerate(points):
            dist = -1*math.sqrt(point[0]**2 + point[1]**2)
            if len(heap) == k:
                heapq.heappushpop(heap, (dist, point))
            else:
                heapq.heappush(heap, (dist, point))
                
        return [point for (dist, point) in heap]
            
        
        

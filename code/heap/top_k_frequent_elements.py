"""
Runtime: 96 ms, faster than 85.44% of Python3 online submissions for Top K Frequent Elements.
Memory Usage: 18.6 MB, less than 76.42% of Python3 online submissions for Top K Frequent Elements.
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        appeared = {}
        cnt = collections.Counter(nums)

        # print(cnt)
        
        heap =  []
        for key, value in cnt.items():
            if len(heap) == k:
                heapq.heappushpop(heap, (value, key))
            else:
                heapq.heappush(heap, (value, key))
        
        return [k for (v, k) in heap]

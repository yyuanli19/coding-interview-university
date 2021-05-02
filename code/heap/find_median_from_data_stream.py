"""
first naive one-heap implementation was too slow
re-implemented with two-heap based on the idea explained here:
https://stackoverflow.com/questions/15319561/how-to-implement-a-median-heap
Runtime: 208 ms, faster than 40.63% of Python3 online submissions for Find Median from Data Stream.
Memory Usage: 25.4 MB, less than 86.23% of Python3 online submissions for Find Median from Data Stream.
"""
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minheap = []
        self.maxheap = []
        self.median = 0

    def addNum(self, num: int) -> None:
        if num > self.median:
            heapq.heappush(self.minheap, num)
        else:
            heapq.heappush(self.maxheap, -1*num)
        
        while len(self.minheap) > len(self.maxheap) +1:
            num = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -1*num)
        
        while len(self.minheap) +1 < len(self.maxheap):
            num = -1*heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, num)
            
        self.median = self.findMedian()
        

    def findMedian(self) -> float:
        #When the min-heap contains one more element than the max-heap, the median is in the top of the min-heap. And when the max-heap contains one more element than the min-heap, the median is in the top of the max-heap.
        if len(self.minheap) == len(self.maxheap) +1:
            return self.minheap[0]
        elif len(self.minheap)+1 == len(self.maxheap):
            return -1*self.maxheap[0]
        else:
            return (self.minheap[0]-self.maxheap[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

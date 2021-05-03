"""
Runtime: 84 ms, faster than 72.94% of Python3 online submissions for Merge Intervals.
Memory Usage: 16.2 MB, less than 10.27% of Python3 online submissions for Merge Intervals.
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = []
        left, right = intervals[0], 1
        while right < len(intervals):
            if left[1] >= intervals[right][0] and left[0] <= intervals[right][1]:
                left = [min(left[0], intervals[right][0]),
                        max(left[1], intervals[right][1])]
            else:
                ans.append(left)
                left = intervals[right]
            
            # print(right, ans)
            right += 1
        ans.append(left)
        return ans
                
        
"""
official answer
Runtime: 80 ms, faster than 89.71% of Python3 online submissions for Merge Intervals.
Memory Usage: 16.2 MB, less than 10.27% of Python3 online submissions for Merge Intervals.
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = []

        for interval in intervals:
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])

        return ans
                
        

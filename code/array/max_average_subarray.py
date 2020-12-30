"""
    official answer 1
    Runtime: 868 ms, faster than 30.42% of Python3 online submissions for Maximum Average Subarray I.
    Memory Usage: 18 MB, less than 61.51% of Python3 online submissions for Maximum Average Subarray I.
"""
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1:
            return float(nums[0])
        if len(nums) <=k:
            return sum(nums)/k
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        #print(nums)
        curr_max = nums[k-1]
        for i in range(k, len(nums)):
            curr_max = max(curr_max, nums[i]-nums[i-k])
        return curr_max/k
    
"""
    official answer 2 + some self solution
    Runtime: 832 ms, faster than 60.23% of Python3 online submissions for Maximum Average Subarray I.
    Memory Usage: 18 MB, less than 61.51% of Python3 online submissions for Maximum Average Subarray I.
"""
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = sum(nums[:k])
        curr_max = curr_sum
        for i in range(k, len(nums)):
            #print(nums[i:i+k])
            curr_sum += nums[i] - nums[i-k]
            curr_max = max(curr_max, curr_sum)
        return curr_max/k
        

"""
    solution founded online
    Runtime: 60 ms, faster than 88.78% of Python3 online submissions for Maximum Subarray.
    Memory Usage: 15.1 MB, less than 9.41% of Python3 online submissions for Maximum Subarray.
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i] = max(nums[i], nums[i-1] + nums[i])
        return max(nums)
        

"""
    found solution divide and conquer
    Runtime: 152 ms, faster than 5.00% of Python3 online submissions for Maximum Subarray.
    Memory Usage: 15.2 MB, less than 9.41% of Python3 online submissions for Maximum Subarray.
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #print("nums: ", nums)
        if len(nums) ==  1 :
            return nums[0]
        elif not nums:
            return 0
        else :
            mid = len(nums)//2
            l_sum = self.maxSubArray(nums[:mid])
            r_sum = self.maxSubArray(nums[mid:])
            c_sum = self.maxcrossingSubArray(nums,mid)
            #print([l_sum,r_sum,c_sum])
            return max(l_sum,r_sum,c_sum)
        
    def maxcrossingSubArray(self,nums,mid):
        max_l_sum = max_r_sum = float('-inf')
        sum = 0
        for i in range(mid-1,-1,-1):
            sum += nums[i]
            max_l_sum = max( max_l_sum ,sum)
        sum = 0

        for i in range(mid,len(nums),1):
            sum += nums[i]
            max_r_sum = max( max_r_sum ,sum)
        return max_l_sum + max_r_sum

        
    


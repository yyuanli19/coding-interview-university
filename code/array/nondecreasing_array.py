"""
    self idea didn't completely work out, had to borrow from the solution
    Runtime: 176 ms, faster than 88.49% of Python3 online submissions for Non-decreasing Array.
    Memory Usage: 15.3 MB, less than 48.96% of Python3 online submissions for Non-decreasing Array.
"""
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        counter = 0
        index = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                counter += 1
                if counter ==2:
                    return False
                index = i
        #print(index)
        if counter == 1:
            return ((index==0) or (index==len(nums)-2) or
               (nums[index-1]<=nums[index+1]) or (nums[index]<=nums[index+2]) )
        return True
        

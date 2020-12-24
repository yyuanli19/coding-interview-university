"""
    Runtime: 9132 ms, faster than 5.04% of Python3 online submissions for 3Sum.
    Memory Usage: 17.8 MB, less than 26.37% of Python3 online submissions for 3Sum.
"""

class Solution:
def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums = sorted(nums)
    #print(nums)
    if len(nums) < 3:
        return []
    anws = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        anw = self.twoSum(nums[:i]+nums[i+1:], -nums[i])
        #print("target: ", -nums[i], "anw: ", anw)
        if len(anw) > 0:
            for a in anw:
                a = sorted([nums[i]] +a)
                if not a in anws:
                    anws.append(a)
            
    return anws
    
def twoSum(self, nums: List[int], target: int) -> List[int]:
    anw = []
    p_small, p_large = 0, len(nums)-1
    while p_small < p_large:
        #print([p_small, p_large])
        tmp_sum = nums[p_small] + nums[p_large]
        if tmp_sum < target:
            p_small += 1
        elif tmp_sum > target:
            p_large -= 1
        else:
            anw.append([nums[p_small], nums[p_large]])
            p_small+=1
            p_large -= 1
    return anw
  
    

    

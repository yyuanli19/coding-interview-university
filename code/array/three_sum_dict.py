
class Solution:
def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums = sorted(nums)
    #print(nums)
    if len(nums) <= 1:
        return []
    anws = []
    for i in range(len(nums)):
        anw = self.twoSum(nums[:i]+nums[i+1:], -nums[i])
        #print("target: ", -nums[i], "anw: ", anw)
        if len(anw) > 0:
            for a in anw:
                a = sorted([nums[i]] +a)
                if not a in anws:
                    anws.append(a)
            
    return anws
    
def twoSum(self, nums: List[int], target: int) -> List[int]:
    dic = {}
    two_anw = []
    for i in range(len(nums)):
        res = target - nums[i]
        if i == 0:
            pass
        elif res in dic.keys():
            two_anw.append([res, nums[i]])
        dic[nums[i]]=i
    return two_anw
  
    

    

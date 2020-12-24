class Solution:
def twoSum(self, nums: List[int], target: int) -> List[int]:
    dic = {}
    for i in range(len(nums)):
        res = target - nums[i]
        if i == 0:
            pass
        elif res in dic.keys():
            return [dic[res], i]
        dic[nums[i]]=i


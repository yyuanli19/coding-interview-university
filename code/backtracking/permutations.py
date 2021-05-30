"""
Runtime: 44 ms, faster than 31.33% of Python3 online submissions for Permutations.
Memory Usage: 14.4 MB, less than 69.91% of Python3 online submissions for Permutations.
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans =[]
        self.backtracking([], nums, ans)
        return ans
        
    def backtracking(self, per, nums, ans):
        if len(per) == len(nums):
            ans.append(per)
        subsets = set(nums) ^ set(per)
        # print(subsets)
        for num in subsets:
            self.backtracking(per+[num], nums, ans)
        
        

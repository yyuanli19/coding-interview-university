"""
Runtime: 36 ms, faster than 48.97% of Python3 online submissions for Subsets.
Memory Usage: 14.7 MB, less than 17.22% of Python3 online submissions for Subsets.
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subsets = []
        self.backtrack(len(nums), [], subsets)
        # print(subsets)
        for subset in subsets:
            tmp = []
            for i in range(len(subset)):
                if subset[i]:
                    tmp.append(nums[i])
            ans.append(tmp)
        return ans
    
    def backtrack(self, n, subset, subsets):
        if len(subset) == n:
            return subsets.append(subset)
        for i in [True, False]:
            self.backtrack(n, subset+[i], subsets)
            
"""
similar idea to above, but with bitmasking
Runtime: 36 ms, faster than 48.97% of Python3 online submissions for Subsets.
Memory Usage: 14.4 MB, less than 49.17% of Python3 online submissions for Subsets.
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        for i in range(2**n, 2**(n + 1)):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i)[3:]
            # print(bin(i))
            # append subset corresponding to that bitmask
            ans.append([nums[j] for j in range(n) if bitmask[j] == '1'])
        
        return ans
        
        

"""
another way of backtracking
Runtime: 36 ms, faster than 48.97% of Python3 online submissions for Subsets.
Memory Usage: 14.4 MB, less than 49.17% of Python3 online submissions for Subsets.
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        for i in range(n+1):
            self.backtrack(0, i, [], nums, ans)
        return ans
    
    def backtrack(self, idx, n, subset, nums, ans):
        if len(subset) == n:
            return ans.append(subset)
        for i in range(idx, len(nums)):
            self.backtrack(i+1, n, subset+[nums[i]], nums, ans)
            ###equivalent to :
            # subset.append(nums[i])
            # self.backtrack(i+1, n, subset, nums, ans)
            # subset.pop()
            
"""
cascading solution
Runtime: 32 ms, faster than 78.25% of Python3 online submissions for Subsets.
Memory Usage: 14.5 MB, less than 49.17% of Python3 online submissions for Subsets.
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for num in nums:
            ans += [curr + [num] for curr in ans]
            ### equivalent to list comprehension
            ### but it is important to deepcopy the ans and loop on the copy,
            ### otherwise the lopp will be endless
            # tmp = ans[:]
            # for curr in tmp:
                # ans += [curr + [num]]
        return ans
     

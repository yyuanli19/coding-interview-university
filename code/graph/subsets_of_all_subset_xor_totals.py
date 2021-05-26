"""
Runtime: 180 ms, faster than 14.61% of Python3 online submissions for Sum of All Subset XOR Totals.
Memory Usage: 14.8 MB, less than 8.27% of Python3 online submissions for Sum of All Subset XOR Totals.
"""
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        sums = 0
        subsets = []
        self.backtrack(len(nums), [], subsets)
        # print(subsets)
        for subset in subsets:
            tmp_sum = 0
            for i in range(len(subset)):
                if subset[i]:
                    tmp_sum ^= nums[i]
                    # print(tmp_sum)
            sums += tmp_sum
        return sums
    
    def backtrack(self, n, subset, subsets):
        if len(subset) == n:
            return subsets.append(subset)
        for i in [True, False]:
            self.backtrack(n, subset+[i], subsets)


"""
optimized version after consulting discussion
Runtime: 60 ms, faster than 77.00% of Python3 online submissions for Sum of All Subset XOR Totals.
Memory Usage: 14.3 MB, less than 37.86% of Python3 online submissions for Sum of All Subset XOR Totals.
"""
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        return self.backtrack(0, 0, nums)

    
    def backtrack(self, i, n, nums):
        if i == len(nums):
            return n
        include = self.backtrack(i + 1, n ^ nums[i], nums)
        exclude = self.backtrack(i + 1, n, nums)
        return include+exclude

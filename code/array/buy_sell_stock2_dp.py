"""
    Runtime: 56 ms, faster than 87.80% of Python3 online submissions for Best Time to Buy and Sell Stock II.
    Memory Usage: 15.1 MB, less than 44.65% of Python3 online submissions for Best Time to Buy and Sell Stock II.
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <=1:
            return 0
        curr_sum, max_sum = 0, 0
        for i in range(1, len(prices)):
            curr_sum = prices[i] - prices[i-1]
            if curr_sum > 0:
                max_sum += curr_sum
                curr_sum = 0
        return max_sum

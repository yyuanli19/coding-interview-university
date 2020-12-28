"""
    solution found online
    Runtime: 68 ms, faster than 27.67% of Python3 online submissions for Best Time to Buy and Sell Stock.
    Memory Usage: 15.1 MB, less than 19.51% of Python3 online submissions for Best Time to Buy and Sell Stock.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <=1:
            return 0
        curr_sum, max_sum = 0, 0
        for i in range(1, len(prices)):
            curr_sum += prices[i] - prices[i-1]
            curr_sum = max(0, curr_sum)
            max_sum = max(max_sum, curr_sum)
        return max_sum
            
"""
    another found solution
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit


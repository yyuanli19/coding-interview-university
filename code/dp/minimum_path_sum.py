"""
Runtime: 124 ms, faster than 17.83% of Python3 online submissions for Minimum Path Sum.
Memory Usage: 15.4 MB, less than 90.40% of Python3 online submissions for Minimum Path Sum.
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # print(len(grid), len(grid[0]))
        for i in range(1, len(grid[0])):
            grid[0][i] += grid[0][i-1]
        for i in range(1, len(grid)):
            grid[i][0] += grid[i-1][0]
            
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        # print(grid)
        return grid[-1][-1]

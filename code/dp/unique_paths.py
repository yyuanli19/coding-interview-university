"""
Runtime: 40 ms, faster than 9.78% of Python3 online submissions for Unique Paths.
Memory Usage: 14.4 MB, less than 36.75% of Python3 online submissions for Unique Paths.
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cos = [[0]*n for _ in range(m)]
        cos[0][:] = [1]*n
        cos[:][0] = [1]*m
        for i in range(m):
            cos[i][0] = 1
        # print(cos)
        for i in range(1, m):
            for j in range(1, n):
                cos[i][j] = cos[i-1][j] + cos[i][j-1]
        # print(cos)
        return cos[-1][-1]
        
"""
optimize the dp table to use less space (use a tmp variable to rember the left moves and thus use only 1-d array.
Runtime: 28 ms, faster than 84.85% of Python3 online submissions for Unique Paths.
Memory Usage: 14.1 MB, less than 85.16% of Python3 online submissions for Unique Paths.
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cos = [1]*n
        for i in range(1, m):
            tmp = 1
            for j in range(1, n):
                cos[j] += tmp
                tmp = cos[j]
        # print(cos)
        return cos[-1]

"""
    Runtime: 32 ms, faster than 49.09% of Python3 online submissions for N-th Tribonacci Number.
    Memory Usage: 14.4 MB, less than 11.74% of Python3 online submissions for N-th Tribonacci Number.
"""
class Solution:
    def tribonacci(self, n: int) -> int:
        mapping = {0:0, 1:1, 2:1}
        return self.dfs(n, mapping)
        
    def dfs(self, n, mapping):
        if n in mapping:
            return mapping[n]
        else:
            mapping[n] = self.dfs(n-1, mapping)+self.dfs(n-2, mapping)+self.dfs(n-3, mapping)
        return mapping[n]
        

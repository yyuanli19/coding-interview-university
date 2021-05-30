"""
Runtime: 28 ms, faster than 79.39% of Python3 online submissions for Count of Matches in Tournament.
Memory Usage: 14.2 MB, less than 35.29% of Python3 online submissions for Count of Matches in Tournament.
"""
class Solution:
    def numberOfMatches(self, n: int) -> int:
        return self.backtracking(n, 0)
    
    def backtracking(self, teams, matches):
        if teams==1:
            return matches
        return self. backtracking(math.ceil(teams/2), matches + teams//2)
        

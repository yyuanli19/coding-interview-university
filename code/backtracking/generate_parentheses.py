"""
Runtime: 112 ms, faster than 5.08% of Python3 online submissions for Generate Parentheses.
Memory Usage: 14.5 MB, less than 65.00% of Python3 online submissions for Generate Parentheses.
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.backtracking("", n, ans)
        # print(ans)
        return ans
        
    def backtracking(self, subset, n, ans):
        if len(subset)==2*n:
            if self.valid(subset):
                ans.append(subset)
            return
        self.backtracking(subset+"(", n, ans)
        self.backtracking(subset+")", n, ans)
        
    def valid(self, par):
        s = 0
        for l in par:
            if l == "(":
                s+=1
            else:
                s-=1
            if s<0:
                return False
        return s==0
        
        
"""
backtracking on number of left and right parenthess, similar to my initial idea, but much better on how to determine which parenthess to add
Runtime: 28 ms, faster than 94.88% of Python3 online submissions for Generate Parentheses.
Memory Usage: 14.7 MB, less than 36.42% of Python3 online submissions for Generate Parentheses.
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.backtracking("", 0, 0, n, ans)
        # print(ans)
        return ans
        
    def backtracking(self, subset, left, right, n, ans):
        if len(subset)==2*n:
            ans.append(subset)
            return
        if left<n:
            self.backtracking(subset+"(", left+1, right, n, ans)
        if right<left:
            self.backtracking(subset+")", left, right+1, n, ans)




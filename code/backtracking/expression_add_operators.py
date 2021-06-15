"""
needed to check answers from discussion
Runtime: 740 ms, faster than 69.16% of Python3 online submissions for Expression Add Operators.
Memory Usage: 14.6 MB, less than 70.15% of Python3 online submissions for Expression Add Operators.
"""
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        ans = []
        self.backtrack(0, num, "", 0, 0, target, ans)
        return ans
        
    def backtrack(self, idx, num, subset, total, last, target, ans):
        if idx == len(num):
            # print(idx, subset, eval(subset) == target)
            if total == target:
                ans.append(subset)
            return
        # print(idx, subset)
        for i in range(idx, len(num)):
            # choose to not add any operand
            n = int(num[idx:i+1])
            if idx == 0:
                self.backtrack(i+1, num, str(n), n, n, target, ans)
            else:
                self.backtrack(i+1, num, subset + '+' + str(n), total + n, n, target, ans)
                self.backtrack(i+1, num, subset + '-' + str(n), total - n, -n, target, ans)
                self.backtrack(i+1, num, subset + '*' + str(n), total - last + last * n, last * n, target, ans)
            if n == 0:
                # in case a 0 is met stop buiding the integer n to avoid cases like 05
                break
  

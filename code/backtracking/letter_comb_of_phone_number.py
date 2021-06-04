"""
Runtime: 32 ms, faster than 53.95% of Python3 online submissions for Letter Combinations of a Phone Number.
Memory Usage: 14.1 MB, less than 95.52% of Python3 online submissions for Letter Combinations of a Phone Number.
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        dic = {"1": [], "2": ["a", "b", "c"], "3": ["d", "e", "f"],
               "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": ["m", "n", "o"],
               "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        # digits = list(digits)
        ans = []
        self.backtrack("", 0, digits, dic, ans)
        # print(ans)
        return ans
        
    def backtrack(self, subset, idx, digits, dic, ans):
        if idx == len(digits):
            return ans.append(subset)

        can = dic[digits[idx]]
        for letter in can:
            self.backtrack(subset+letter, idx+1, digits, dic, ans)
            
"""
initial idea of using cascading didn't work because I didn't know how to generate comb of exactly length m, consulted discussion.
Runtime: 28 ms, faster than 81.35% of Python3 online submissions for Letter Combinations of a Phone Number.
Memory Usage: 14.2 MB, less than 84.85% of Python3 online submissions for Letter Combinations of a Phone Number.
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        dic = {"1": [], "2": ["a", "b", "c"], "3": ["d", "e", "f"],
               "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": ["m", "n", "o"],
               "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        # digits = list(digits)
        ans = [''] if digits else []
        for digit in digits:
            tmp_ans = []
            for letter in dic[digit]:
                for combination in ans:
                    tmp_ans.append(combination + letter)
            ans = tmp_ans
        return ans

"""
    Runtime: 44 ms, faster than 59.64% of Python3 online submissions for Fizz Buzz.
    Memory Usage: 15.2 MB, less than 24.31% of Python3 online submissions for Fizz Buzz.
"""
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n+1):
            if i%15 == 0:
                res.append("FizzBuzz")
            elif i%3 == 0:
                res.append("Fizz")
            elif i%5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res
        

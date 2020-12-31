"""
    idea was right, but couldn't work out an accepted solutionm. checked for solution
    Runtime: 132 ms, faster than 68.38% of Python3 online submissions for X of a Kind in a Deck of Cards.
    Memory Usage: 14.4 MB, less than 88.53% of Python3 online submissions for X of a Kind in a Deck of Cards.
"""
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        dic = {}
        for i in deck:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        count = list(dic.values())
        return reduce(gcd, count) > 1
def gcd(a, b):
    while b: a, b = b, a % b
    return a
        
        

"""
    my first medium problem, sadly solve brute forcely, yet the hint suggests so
    Runtime: 588 ms, faster than 55.95% of Python3 online submissions for Count Number of Teams.
    Memory Usage: 14.4 MB, less than 26.38% of Python3 online submissions for Count Number of Teams.
"""
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        num = 0
        min1, min2 = float("-inf"), float("-inf")
        max1, max2 = float("inf"), float("inf")
        for i in range(len(rating)):
            for j in range(i, len(rating)):
                if rating[j] > rating[i]:
                    for z in range(j, len(rating)):
                        if rating[z] > rating[j]:
                            num+=1
                elif rating[j] < rating[i]:
                    for z in range(j, len(rating)):
                        if rating[z] < rating[j]:
                            num+=1
                    
        return num
       

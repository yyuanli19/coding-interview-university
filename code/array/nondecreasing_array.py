"""
    self idea didn't completely work out, had to borrow from the solution
    Runtime: 176 ms, faster than 88.49% of Python3 online submissions for Non-decreasing Array.
    Memory Usage: 15.3 MB, less than 48.96% of Python3 online submissions for Non-decreasing Array.
"""
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        counter = 0
        index = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                counter += 1
                if counter ==2:
                    return False
                index = i
        #print(index)
        if counter == 1:
            return ((index==0) or (index==len(nums)-2) or
               (nums[index-1]<=nums[index+1]) or (nums[index]<=nums[index+2]) )
        return True
        

"""
    added another solution found in discussion that fits better my original idea
    Runtime: 136 ms, faster than 45.90% of Python3 online submissions for X of a Kind in a Deck of Cards.
    Memory Usage: 14.6 MB, less than 38.15% of Python3 online submissions for X of a Kind in a Deck of Cards.
"""
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        dic = {}
        for i in deck:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        m = min(dic.values())
        if m <= 1:
            return False
        for i in range(m, 1, -1):
            if sum([x%i for x in dic.values()]) == 0:
                return True
        return False
         

        

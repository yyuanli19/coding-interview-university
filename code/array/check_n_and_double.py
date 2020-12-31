
"""
    Runtime: 56 ms, faster than 40.02% of Python3 online submissions for Check If N and Its Double Exist.
    Memory Usage: 14.4 MB, less than 39.18% of Python3 online submissions for Check If N and Its Double Exist.
"""
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        dic ={}
        for i in arr:
            if i in dic:
                dic[i] +=1
            else:
                dic[i] = 1
        for i in arr:
            if i == 0 and dic[0] > 1:
                return True
            elif i!=0 and i*2 in dic:
                return True
        return False

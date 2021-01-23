"""
    time： 480ms 97.95%
    mem:  18.7MB  62.53%
"""
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        res = [0]*len(T)
        for i, temp in enumerate(T):
            while stack and T[stack[-1]] < temp:
                day = stack.pop()
                res[day] = i- day
            stack.append(i)
            # print(stack)
        return res
        
        
        

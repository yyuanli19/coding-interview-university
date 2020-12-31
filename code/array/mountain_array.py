"""
    Runtime: 204 ms, faster than 51.04% of Python3 online submissions for Valid Mountain Array.
    Memory Usage: 15.6 MB, less than 9.81% of Python3 online submissions for Valid Mountain Array.
"""
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        top = None
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                return False
            elif arr[i] > arr[i+1] and top is None:
                top = i
            elif arr[i] < arr[i+1] and top is not None:
                return False
        return (top is not None and top != 0)
            
        

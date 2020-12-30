"""
    Runtime: 164 ms, faster than 73.30% of Python3 online submissions for Can Place Flowers.
    Memory Usage: 14.7 MB, less than 35.97% of Python3 online submissions for Can Place Flowers.
"""
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        counter, total_available = 0, 0
        flowerbed = [0] + flowerbed + [0]
        for i in flowerbed:
            if i!=0:
                counter = 0
            else:
                counter += 1
                
            if counter == 3:
                total_available+= 1
                counter = 1
        if total_available >= n:
            return True
        else:
            return False
        

"""
    Runtime: 92 ms, faster than 90.48% of Python3 online submissions for Reshape the Matrix.
    Memory Usage: 15.3 MB, less than 35.19% of Python3 online submissions for Reshape the Matrix.
"""
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        o_r, o_c = len(nums), len(nums[0])
        if o_r*o_c != r*c:
            return nums
        else:
            new_matrix = []
            for i in range(r):
                row = []
                for j in range(c):
                    row.append(nums[(c*i+j)//o_c][(c*i+j)%o_c])
                new_matrix.append(row)
            return new_matrix
                
        

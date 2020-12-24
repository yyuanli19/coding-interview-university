"""
    Runtime: 32 ms
    Memory Usage: 14.4 MB
"""
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            rows = []
            for i in range(rowIndex+1):
                row = [1 for _ in range(i+1)]
                if i > 1:
                    for j in range(1, i):
                        row[j] = rows[i-1][j-1] + rows[i-1][j]
                   #print("row: ", row)
                rows.append(row)
            return row
    
"""
    solution found online that uses O(k) memory
    Runtime: 24 ms, faster than 95.92% of Python3 online submissions for Pascal's Triangle II.
    Memory Usage: 14.1 MB, less than 87.57% of Python3 online submissions for Pascal's Triangle II.
"""
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        row = [1 for _ in range(rowIndex+1)]
        for i in range(1, rowIndex):
            for j in range(i, 0, -1):
                row[j] += row[j-1]
            #print("i, row: ", i, row)
        return row
            
        


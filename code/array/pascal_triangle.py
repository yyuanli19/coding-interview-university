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

"""
another very similar version
    Runtime: 20 ms, faster than 99% of Python3 online submissions for Pascal's Triangle.
    Memory Usage: 14.2 MB, less than 81.34% of Python3 online submissions for Pascal's Triangle.
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        rows = [[1], [1,1]]
        for i in range(3, numRows+1):
            row= []
            for j in range(i):
                if j-1<0 or j==i-1:
                    row.append(1)
                else:
                    # print(i, j, rows[-1])
                    row.append(rows[-1][j-1]+rows[-1][j])
            rows.append(row)
        return rows
        
            
        


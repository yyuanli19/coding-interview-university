
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        org = image[sr][sc]
        return self.dfs(image, sr, sc, org, newColor)

    def dfs(self, image, sr, sc, oldColor, newColor):
        row, col = len(image), len(image[0])
        if oldColor == newColor:
            return image
        for i,j in [(sr-1, sc), (sr, sc-1), (sr, sc),
                   (sr, sc+1), (sr+1, sc)]:
            if (0<=i<row) and (0<=j<col) and (image[i][j] == oldColor):
                image[i][j] = newColor
                # print(i, j, image, visited)
                self.dfs(image, i, j, oldColor, newColor)
        return image
        

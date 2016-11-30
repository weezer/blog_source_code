Title: 64. Minimum Path Sum 
Date: 2016-11-02 00:31
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-64_Minimum_Path_Sum 
Authors: Weezer Su
Summary: Minimum Path Sum


```python
class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        yLen = len(grid[0])
        xLen = len(grid)
        ma = [[0 for i in range(yLen)] for j in range(xLen)]
        ma[0][0] = grid[0][0]
        if xLen > 1 :
            for i in range(1, xLen):
                ma[i][0] = ma[i-1][0] + grid[i][0]
        if yLen > 1:
            for j in range(1, yLen):
                ma[0][j] = ma[0][j-1] + grid[0][j]
        if xLen > 1 and yLen > 1:
            for i in range(1, xLen):
                for j in range(1, yLen):
                    ma[i][j] = min(ma[i-1][j] + grid[i][j], ma[i][j-1] + grid[i][j])
                    
        return ma[xLen - 1][yLen - 1]
```


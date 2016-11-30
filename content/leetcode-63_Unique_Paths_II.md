Title: 63. Unique Paths II 
Date: 2016-11-02 00:27
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-63_Unique_Paths_II 
Authors: Weezer Su
Summary: Unique Paths II


```python
class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        matrix = [[0 for i in range(len(obstacleGrid[0]) + 1)] for j in range(len(obstacleGrid) + 1)]
        # for i in range(len(matrix)):
        #     matrix[i][0] = 0
        matrix[0][1] = 1
        for i in range(1, len(obstacleGrid) + 1):
            for j in range(1, len(obstacleGrid[0]) + 1):
                if obstacleGrid[i-1][j-1] == 1:
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        return matrix[i][j]
```


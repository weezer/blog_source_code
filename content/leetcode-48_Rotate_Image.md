Title: 48. Rotate Image 
Date: 2016-10-16 14:12
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-48_Rotate_Image 
Authors: Weezer Su
Summary: Rotate Image

in place and new matrix

```python
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        newMatrix = [[0 for x in range(len(matrix))] for y in range(len(matrix))]

        n = len(matrix) - 1
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                newMatrix[j][n] = matrix[i][j]
            n -= 1

        return newMatrix


    def inplacerotate(self, matrix):
        n = len(matrix) - 1
        for i in range(len(matrix)/2):
            tmp = matrix[i]
            matrix[i] = matrix[n - i]
            matrix[n - i] = tmp

        n = 1
        for i in range(len(matrix)):
            for j in range(n, len(matrix)):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
            n += 1

        print matrix
```


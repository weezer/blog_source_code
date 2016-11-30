Title: 73. Set Matrix Zeroes 
Date: 2016-11-04 00:22
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-73_Set_Matrix_Zeroes 
Authors: Weezer Su
Summary: Set Matrix Zeroes


```python
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        firstRowContains0 = False  
        for row in matrix[0] :  
            if row == 0 :   
                firstRowContains0 = True  
                break  
        for i in range(1,len(matrix)) :  
            thisRowContains0 = False  
            for j in range(0, len(matrix[0])) :  
                if matrix[i][j] == 0 :  
                    thisRowContains0 = True  
                    matrix[0][j] = 0  
            if thisRowContains0 :  
                for j in range(0, len(matrix[0])) :  
                    matrix[i][j] = 0  
        for j in range(len(matrix[0])) :  
            if matrix[0][j] == 0 :  
                for i in range(len(matrix)) :  
                    matrix[i][j] = 0  
        if firstRowContains0 :  
            for j in range(len(matrix[0])) :  
                matrix[0][j] = 0  
```


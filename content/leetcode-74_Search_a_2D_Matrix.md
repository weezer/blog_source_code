Title: 74. Search a 2D Matrix 
Date: 2016-11-29 22:07
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-74_Search_a_2D_Matrix 
Authors: Weezer Su
Summary: Search a 2D Matrix
```python
class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0:
            return False
            
        n, m = len(matrix), len(matrix[0])
        start, end = 0, n * m - 1
        while start + 1 < end:
            mid = (start + end) / 2
            x, y = mid / m, mid % m
            if matrix[x][y] < target:
                start = mid
            else:
                end = mid
        x, y = start / m, start % m
        if matrix[x][y] == target:
            return True
        
        x, y = end / m, end % m
        if matrix[x][y] == target:
            return True
        
        return False
```

二分搜索两次, 时间会爆，想想其实二分就可以了，就相当于把一个一维排序的拆成好几段。
```python
class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        xLen = len(matrix)
        yLen = len(matrix[0])
        
        if target < matrix[0][0] or target > matrix[xLen - 1][0]:
            return False
        
        minPos = 0
        maxPos = xLen - 1
        while minPos <= maxPos:
            if target > matrix[(minPos + maxPos)/2][0]:
                minPos = (minPos + maxPos)/2 + 1
            elif target < matrix[(minPos + maxPos)/2][0]:
                maxPos = (minPos + maxPos)/2
        return findY(target, matrix[(minPos + maxPos)/2 - 1])
        
    def findY(self, target, aList):
        found = False
        length = yLen
        minPos = 0
        maxPos = length - 1
        while minPos <= maxPos:
            if target > aList[(minPos + maxPos)/2]:
                minPos = (minPos + maxPos)/2 + 1
            elif target < aList[(minPos + maxPos)/2]:
                maxPos = (minPos + maxPos)/2
            elif target == aList[(minPos + maxPos)/2]:
                found = True
                break
        return found
```


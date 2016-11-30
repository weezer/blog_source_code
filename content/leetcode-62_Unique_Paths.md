Title: 62. Unique Paths 
Date: 2016-11-01 23:40
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-62_Unique_Paths 
Authors: Weezer Su
Summary: Unique Paths

对于m行n列的矩形，从左上角走到右下角需要走m-1+n-1步，其中m-1步是向下的，n-1步是向右的，这m-1+n-1步中的向下和向右任意组合，很明显存在的路径个数是组合数C(m-1+n-1, m-1)。
    从图的角度来看，可以采用由小到大的递推思想进行，先考虑最接近右下角的点到目的地的路径个数，然后依次递推，逐步扩散直到左上角。
```python
class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        if m == 1 or n == 1:
            return 1
        num = reduce(lambda x, y : x*y, range(1, m+n-1))
        num1 = reduce(lambda x, y : x*y, range(1, m))
        num2 = reduce(lambda x, y : x*y, range(1, n))
        return num/(num1*num2)
```

还是用常规的动规吧。

```python
class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        if m == 1 or n == 1:
            return 1
        matrix = [[1 for i in range(m)] for j in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        return matrix[n-1][m-1]
```

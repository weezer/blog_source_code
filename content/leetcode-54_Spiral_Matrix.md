Title: 54. Spiral Matrix 
Date: 2016-10-31 22:37
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-54_Spiral_Matrix 
Authors: Weezer Su
Summary: Spiral Matrix

太恶心了，我还是应该用方向的。
```python
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        total_num = m*n
        matrix_lst = []
        count, i, j = 0, 0, 0
        while count < n:
            for j in range(count, n):
                matrix_lst.append(matrix[i][j])
            n -= 1
            if len(matrix_lst) == total_num:
                break
            for i in range(count+1, m):
                matrix_lst.append(matrix[i][j])
            m -= 1
            if len(matrix_lst) == total_num:
                break
            for j in range(n-1, count-1, -1):
                matrix_lst.append(matrix[i][j])
            if len(matrix_lst) == total_num:
                break
            for i in range(m-1, count, -1):
                matrix_lst.append(matrix[i][j])
            count += 1

        return matrix_lst
```
for fun
```python
def printspiral(n):
    n2list = [i for i in range(n**2)][::-1]
    # print n2list
    print makespiral(n2list)


def makespiral(lst):
    lst_len = len(lst)
    num_perline = int(lst_len ** 0.5)
    makeupmatrix = [[0 for i in range(num_perline)] for j in range(num_perline)]
    count, i, j = 0, 0, 0
    while count < num_perline:
        print lst
        for j in range(count, num_perline):
            makeupmatrix[i][j] = lst.pop()
        for i in range(count+1, num_perline):
            makeupmatrix[i][j] = lst.pop()
        for j in range(num_perline-2, count-1, -1):
            makeupmatrix[i][j] = lst.pop()
        for i in range(num_perline-2, count, -1):
            makeupmatrix[i][j] = lst.pop()
        print makeupmatrix
        count += 1
        num_perline -= 1
    return makeupmatrix


printspiral(4)
```

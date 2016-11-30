Title: 75. Sort Colors 
Date: 2016-11-29 23:32
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-75_Sort_Colors.md 
Authors: Weezer Su
Summary: Sort Colors

计数
```python
class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        i, j, k = -1, -1, -1
        for num in A:
            if num == 0:
                k += 1
                A[k] = 2
                j += 1
                A[j] = 1
                i += 1
                A[i] = 0
            if num == 1:
                k += 1
                A[k] = 2
                j += 1
                A[j] = 1
            if num == 2:
                k += 1
                A[k] = 2
```


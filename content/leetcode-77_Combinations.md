Title: 77. Combinations 
Date: 2016-11-30 11:46
Category: leetcode
Tags: code, python, leetcode
Slug:leetcode-77_Combinations 
Authors: Weezer Su
Summary: Combinations
下面这个会陷入死循环
```python
a = [1]
for i in a:
    a.append(123)
```
所以需要用position来定位

```python
class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        A = [[]]
        S = [i for i in range(1, n+1)]
        for i in S:
            for j in range(len(A)):
                ss = A[j][:]
                ss.append(i)
                A.append(ss)
        return [i for i in A if len(i) == k]
```


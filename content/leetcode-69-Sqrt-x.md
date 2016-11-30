Title: 69. Sqrt(x) 
Date: 2016-11-02 23:01
Category: leetcode
Tags: code, python, leetcode
Slug: 69-leetcode-Sqrt_x 
Authors: Weezer Su
Summary: Sqrt(x)


```python
class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            tmp = mid * mid
            if tmp == x:
                return mid
            if tmp > x:
                right = mid - 1
            if tmp < x:
                left = mid + 1
        return right
```


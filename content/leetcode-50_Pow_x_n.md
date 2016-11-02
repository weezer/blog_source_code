Title: 50. Pow(x, n)  
Date: 2016-10-16 14:43
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-50_Pow_x_n 
Authors: Weezer Su
Summary: Pow(x, n)
5*5*5*5 = 25 * 25

```python
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0
        elif n < 0:
            return 1 / self.myPow(x, -n)
        elif n % 2 == 1:
            return self.myPow(x*x, n/2)*x
        else:
            return self.myPow(x*x, n/2)
```


Title: 07. Reverse Integer
Date: 2016-09-16 1:38
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-7-Reverse_Integer
Authors: Weezer Su
Summary:  Reverse Integer

Well pythonic doesn't care about the boundary of integer or whatever, but if you want to submit a answer on leetcode
you have to enter the boundary for this question.


```python
class Solution:
    # @return an integer
    def reverse(self, x):
        newN = 0
        sym = 1
        if x < 0:
            x = -x
            sym = -1
        while x != 0:
            answer = x % 10
            newN = newN * 10 + answer
            x /= 10
        #stupid question because dumb c or c++ coder.            
        if newN * sym < -(1 << 31) or newN * sym > (1 << 31) - 1:
            return 0
        return newN * sym
```

```
Binary    Weighted sum            Integer value
0000       0 + 0 + 0 + 0           0
0001       0 + 0 + 0 + 2^0         1
0010       0 + 0 + 2^1 + 0         2
0011       0 + 0 + 2^1 + 2^0       3
0100       0 + 2^2 + 0 + 0         4
0101       0 + 2^2 + 0 + 2^0       5
0110       0 + 2^2 + 2^1 + 0       6
0111       0 + 2^2 + 2^1 + 2^0     7 -> the most positive value
1000      -2^3 + 0 + 0 + 0        -8 -> the most negative value
1001      -2^3 + 0 + 0 + 2^0      -7
1010      -2^3 + 0 + 2^1 + 0      -6
1011      -2^3 + 0 + 2^1 + 2^0    -5
1100      -2^3 + 2^2 + 0 + 0      -4
1101      -2^3 + 2^2 + 0 + 2^0    -3
1110      -2^3 + 2^2 + 2^1 + 0    -2
1111      -2^3 + 2^2 + 2^1 + 2^0  -1
```

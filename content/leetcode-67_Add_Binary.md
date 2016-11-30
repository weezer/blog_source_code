Title: 67. Add Binary
Date: 2016-11-02 9:24
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-67_Add_Binary 
Authors: Weezer Su
Summary: Add Binary


```python

```

就是学习一下int
```python
class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]
```


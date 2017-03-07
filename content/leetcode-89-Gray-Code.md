Title: 89. Gray Code 
Date: 2017-02-21 15:43
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-89-Gray-Code 
Authors: Weezer Su
Summary: 89. Gray Code


```python
ass Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        lst = ['0', '1']
        dummy_lst = []
        if n == 0:
            return [0]
        if n == 1:
            return map(int, lst)
        while n > 1:
            for i in lst:
                dummy_lst.append('0' + i)
            for i in lst[::-1]:
                dummy_lst.append('1' + i)
            lst = dummy_lst[:]
            dummy_lst = []
            n -= 1
        return map(lambda x: int(x, 2), lst)
```


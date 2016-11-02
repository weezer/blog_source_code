Title: 60. Permutation Sequence 
Date: 2016-11-01 20:50
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-60_Permutation_Sequence 
Authors: Weezer Su
Summary: Permutation Sequence
这是数学方法。
```python
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        result_str = ""
        x = [str(i) for i in range(1, n+1)]
        while len(x) > 0:
            fac_result = self.factorial(n-1)
            for i in range(1, n+1):
                if i * fac_result >= k:
                    result_str += x.pop(i-1)
                    k -= (i-1) * fac_result
                    n -= 1
                    break

        return result_str

    def factorial(self, n):
        result = 1
        while n > 1:
            result *= n
            n -= 1
        return result
```

如果用permutation的方法会超时
```python
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        x = [str(i) for i in range(1, n+1)]
        aStack = [x.pop()]
        bStack = []
        for i in x:
            elementlength = len(aStack[-1])
            while len(aStack) > 0:
                current = aStack.pop()
                for pos in range(elementlength + 1):
                    bStack.append(current[:pos] + i + current[pos:])
            aStack = bStack[:]
            bStack = []
        aStack.sort()
        return aStack[k-1]
```


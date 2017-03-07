Title:96. Unique Binary Search Trees 
Date: 2017-02-28 12:47
Category: leetcode
Tags: code, python, leetcode
Slug:leetcode-96-Unique-Binary-Search-Trees 
Authors: Weezer Su
Summary: Unique Binary Search Trees 

```python
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1] * (n + 1)
        for i in range(n):
            dp[i] = sum([dp[i-pos-1] * dp[pos] for pos in range(i)])
        print dp[n]
```


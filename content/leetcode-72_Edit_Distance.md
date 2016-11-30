Title: 72. Edit Distance 
Date: 2016-11-03 23:07
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-72_Edit_Distance 
Authors: Weezer Su
Summary: Edit Distance

动态规划
```python
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if len(word1) == 0 or len(word2) == 0:
            return max(len(word1), len(word2))
        else:
            result = [[max(i, j) for i in range(len(word1) + 1)] for j in range(len(word2) + 1)]
        print result
        for i in range(1, len(word2)+1):
            for j in range(1, len(word1)+1):
                if word2[i-1] == word1[j-1]:
                    result[i][j] = result[i-1][j-1]
                else:
                    result[i][j] = min((result[i-1][j] + 1), (result[i][j-1] + 1), (result[i-1][j-1] + 1))
        print result
        return result[i][j]
```


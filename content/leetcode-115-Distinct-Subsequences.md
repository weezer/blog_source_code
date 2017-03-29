Title: 115. Distinct Subsequences
Date: 2017-03-28 21:34:26
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-115-Distinct-Subsequences
Authors: Weezer Su
Summary: 115. Distinct Subsequences


```python
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        s_len = len(s)
        t_len = len(t)
        matrix = [[0 for i in range(s_len + 1)] for j in range(t_len + 1)]

        for i in range(len(s) + 1):
            matrix[0][i] = 1

        for i in range(1, t_len+1):
            for j in range(1, s_len+1):
                if s[j-1] == t[i-1]:
                    matrix[i][j] = matrix[i][j-1] + matrix[i-1][j-1]
                else:
                    matrix[i][j] = matrix[i][j-1]
        return matrix[i][j]

if __name__ == "__main__":
    s = Solution()
    print s.numDistinct("rabbasdasdsadbit", "rabbit")
```

```

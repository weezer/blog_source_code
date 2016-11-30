Title: 70. Climbing Stairs 
Date: 2016-11-02 23:42
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-70_Climbing_Stairs 
Authors: Weezer Su
Summary: Climbing Stairs


```pythoni
class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        stepLst = [1] * (n+1)
        start = 2
        while start <= n:
            stepLst[start] = stepLst[start-1] + stepLst[start-2]
            start += 1
        # print stepLst
        return stepLst[n]
            
```


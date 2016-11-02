Title: 42. Trapping Rain Water 
Date: 2016-10-13 23:19
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-42_Trapping_Rain_Water 
Authors: Weezer Su
Summary: Trapping Rain Water

Naive solution, can't pass it.


```python
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        size = 0
        for i in range(1, len(height)):
            left = max(height[:i])
            right = max(height[i:])
            if height[i] < min(left, right):
                size += min(left, right) - height[i]
        return size
        
```


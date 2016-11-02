Title: 11. Container With Most Water 
Date: 2016-09-17 23:13
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-11-Container_With_Most_Water 
Authors: Weezer Su
Summary: Container With Most Water

Wired, should i consider the 0 value in the list? 


```python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        end = len(height) - 1
        start = 0
        max_volume = 0
        while end > start:
            if height[end] >= height[start]:
                v_height = height[start]
                start += 1
            else:
                v_height = height[end]
                end -= 1
            if max_volume < (end - start + 1) * v_height:
                max_volume = (end - start + 1) * v_height
        return max_volume
```

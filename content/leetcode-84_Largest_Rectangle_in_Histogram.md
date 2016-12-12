Title:84. Largest Rectangle in Histogram 
Date: 2016-12-07 01:58
Category: leetcode
Tags: code, python, leetcode
Slug:leetcode-84_Largest_Rectangle_in_Histogram 
Authors: Weezer Su
Summary: Largest Rectangle in Histogram


```python
class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        dummyStack = height[:] + [0]
        stack = []
        largest = 0
        pos = 0
        while pos < len(dummyStack):
            if not stack or dummyStack[pos] > dummyStack[stack[-1]]:
                stack.append(pos)
                pos += 1
            else:
                cur = stack.pop()
                largest = max(largest,  height[cur]*( not stack and pos or pos - stack[-1] - 1))
        
        return largest
```


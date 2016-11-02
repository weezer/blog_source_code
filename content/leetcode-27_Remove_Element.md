Title: 27. Remove Element 
Date: 2016-09-21 21:27
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-27_Remove_Element 
Authors: Weezer Su
Summary: Remove Element


```python
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        new_count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                continue
            nums[new_count] = nums[i]
            new_count += 1
        return new_count
```


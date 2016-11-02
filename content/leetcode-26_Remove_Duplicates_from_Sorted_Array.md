Title: 26. Remove Duplicates from Sorted Array 
Date: 2016-09-21 21:17
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-26_Remove_Duplicates_from_Sorted_Array 
Authors: Weezer Su
Summary: Remove Duplicates from Sorted Array

2 points.

```python
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        new_count = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[new_count]:
                new_count += 1
                if new_count != i:
                    nums[new_count] = nums[i]
        new_count += 1
        return new_count
                
```


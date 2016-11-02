Title: 35. Search Insert Position 
Date: 2016-09-29 21:39
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-35_Search_Insert_Position 
Authors: Weezer Su
Summary: Search Insert Position

Dont think its a medium level.


```python
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if len(nums) == 0:
            return 0
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if target <= nums[left]:
                return left
            if target == nums[right]:
                return right
            if target > nums[right]:
                return right + 1
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                left = mid + 1
            if target < nums[mid]:
                right = mid - 1
```


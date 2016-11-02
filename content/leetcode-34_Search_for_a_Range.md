Title: 34. Search for a Range 
Date: 2016-09-28 00:10
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-34_Search_for_a_Range  
Authors: Weezer Su
Summary: Search for a Range

Hate this kind of question


```python
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]
        left = self.findtheleft(nums, target)
        right = self.findtheright(nums, target)
        return [left, right]

    def findtheleft(self, nums, target):
        left = 0
        right = len(nums) - 1
        if nums[left] == target:
            return left
        if nums[left] > target:
            return -1
        while left <= right:
            mid = (left + right) / 2
            if mid > 0:
                if nums[mid - 1] < target and nums[mid] == target:
                    return mid
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def findtheright(self, nums, target):
        left = 0
        right = len(nums) - 1
        if nums[right] == target:
            return right
        if nums[right] < target:
            return -1
        while left <= right:
            mid = (left + right) / 2
            if mid < len(nums) - 1:
                if nums[mid + 1] > target and nums[mid] == target:
                    return mid
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1
```


Title: 81. Search in Rotated Sorted Array II 
Date: 2016-12-01 23:25
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-81_Search_in_Rotated_Sorted_Array_II 
Authors: Weezer Su
Summary: Search in Rotated Sorted Array II

边界判断，一个需要等于最小，一个需要等于最大。逻辑判断，想不通的就让电脑想，抓最重要的部分。
```python
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] == target:
                return True
            if nums[mid] > nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < nums[left]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                left += 1
        return False
```


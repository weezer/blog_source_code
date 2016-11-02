Title: 33. Search in Rotated Sorted Array 
Date: 2016-09-23 23:02
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-33_Search_in_Rotated_Sorted_Array 
Authors: Weezer Su
Summary: Search in Rotated Sorted Array

little snippet if you need to test in your IDE, may help you to rotate a list

```python
def rotate(l, n):
    return l[-n:] + l[:-n]
```


```python

class BinarySearchRotate(object):
    def binarySearchRotate(self, nums, target):
        left = 0
        right = len(nums) - 1
        mid = (left + right) / 2
        while left <= right:
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[left] and nums[mid] > nums[right]:
                if nums[left] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            mid = (left + right) / 2
            print left, right
        return -1
```


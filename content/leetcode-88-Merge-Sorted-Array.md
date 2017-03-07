Title: 88. Merge Sorted Array 
Date: 2017-02-21 14:17
Category: leetcode
Tags: code, python, leetcode
Slug:leetcode-88-Merge-Sorted-Array 
Authors: Weezer Su
Summary: 88. Merge Sorted Array

傻逼题
```python
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1.sort()
```


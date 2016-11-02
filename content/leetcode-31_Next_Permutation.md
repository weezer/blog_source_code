Title: 31. Next Permutation
Date: 2016-09-23 01:10
Category: leetcode
Tags: code, python, leetcode
Slug:leetcode-31_Next_Permutation 
Authors: Weezer Su
Summary: Next Permutation

Can't believe i spent hours on this one. dumb.


```python
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return

        left = len(nums) - 1
        change = False
        while left > 0:
            left -= 1
            comp_pos = left
            for i in range(left + 1, len(nums)):
                if nums[i] > nums[left]:
                    if comp_pos is left:
                        comp_pos = i
                    if nums[i] < nums[comp_pos]:
                        comp_pos = i
            if nums[left] < nums[comp_pos]:
                temp = nums[left]
                nums[left] = nums[comp_pos]
                nums[comp_pos] = temp
                change =True
                break

        start = len(nums) - 1
        if change:
            end = left
        else:
            end = -1
        for i in range(start, end, -1):
            for j in range(end + 1, i):
                if nums[j] > nums[i]:
                    nums[j] += nums[i]
                    nums[i] = nums[j] - nums[i]
                    nums[j] -= nums[i]
```


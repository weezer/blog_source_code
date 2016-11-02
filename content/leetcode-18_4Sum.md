Title: 18. 4Sum 
Date: 2016-09-20 23:52
Category: leetcode
Tags: code, python, leetcode
Slug:leetcode-18_4Sum 
Authors: Weezer Su
Summary: 4 Sum to K-sum

for all k-sum question, you can think like a k + k(-1) question, and use 2 point for the 2 sum.

```python
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result_set = []
        if len(nums) < 4:
            return result_set
        nums.sort()
        for i in range(len(nums) - 3):
            if i and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = len(nums) - 1

                while left < right:
                    if target == nums[i] + nums[j] + nums[left] + nums[right]:
                        result_set.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[right + 1] == nums[right]:
                            right -= 1
                        while left < right and nums[left - 1] == nums[left]:
                            left += 1
                    elif target < nums[i] + nums[j] + nums[left] + nums[right]:
                        right -= 1
                    else:
                        left += 1

        return result_set
```


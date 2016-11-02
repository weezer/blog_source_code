Title: 53. Maximum Subarray 
Date: 2016-10-31 00:31
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-53_Maximum_Subarray.md 
Authors: Weezer Su
Summary: Maximum Subarray
Improved
```python
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_value = -1 << 31
        tmp_sum = 0
        max_list = [nums[0]]
        for i in nums:
            tmp_sum = max(tmp_sum + i, i)
            max_value = max(max_value, tmp_sum)
        return max_value
```

```python
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = []
        max_list = []
        ret_val = 0
        max_val = 0
        for i in nums:
            if len(max_list) == 0:
                max_list = [i]
                max_val = i
            else:
                max_val = max(max_val, i)
            if i > 0 or len(ret) > 0:
                ret.append(i)
                ret_val += i
            if ret_val > max_val and len(ret) > 0:
                max_list = ret[:]
                max_val = ret_val
            if ret_val < 0:
                ret = []
                ret_val = 0
        return max_val
```


Title: 55. Jump Game 
Date: 2016-10-31 22:47
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-55_Jump_Game 
Authors: Weezer Su
Summary: Jump Game


渣渣
```python
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        jump = 0
        length = len(nums)
        for pos, val in enumerate(nums):
            jump = max(val, jump-1)
            if pos + jump >= length-1:
                return True
            if jump == 0:
                return False
        return False
            
```


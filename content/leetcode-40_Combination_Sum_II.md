Title: 40. Combination Sum II 
Date: 2016-10-01 1:1
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-40_Combination_Sum_II 
Authors: Weezer Su
Summary: Combination Sum II

If will create a new parameter(a copy), it wont change the argument which passed to it. 


```python
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = candidates
        self.result = []
        self.combinationMethod([], nums, target)
        return self.result

    def combinationMethod(self, current_nums, nums, target):
        for i in range(len(nums)):
            if sum(current_nums) + nums[i] == target:
                answer_nums = current_nums[:]
                answer_nums.append(nums[i])
                answer_nums.sort()
                if answer_nums not in self.result:
                    self.result.append(answer_nums)
            if sum(current_nums) + nums[i] < target:
                remain_nums = nums[i+1:]
                answer_nums = current_nums[:]
                answer_nums.append(nums[i])
                self.combinationMethod(answer_nums, remain_nums, target)
```


Title: 15. 3Sum 
Date: 2016-09-19 00:03
modified: 2016-09-19 13:40
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-15_3Sum 
Authors: Weezer Su
Summary: 3Sum

I tried DPS, but the time complexity is too high, check the answer and the sorted then minus is the best practise.

```python
class Solution(object):
    def threeSum(self, nums):
        """
	DPS, time complexity is too high
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        self.recursive_dump([], nums)
        return self.result

    def recursive_dump(self, cal_lst, r_lst):
        if len(cal_lst) == 3:
            if sum(cal_lst) == 0 and sorted(cal_lst) not in self.result:
                return self.result.append(sorted(cal_lst))
            else:
                return None
        if len(cal_lst) > 3:
            return
        for i in r_lst:
            cl_lst = cal_lst + [i]
            rm_lst = r_lst[:]
            rm_lst.remove(i)
            self.recursive_dump(cl_lst, rm_lst)
```

Best Solution, 3 index, then eliminate those replicans.

```python
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []

        if len(nums) < 3:
            return result

        for i in range(len(nums) - 2):
            if i == 0 or nums[i] > nums[i-1]:
                left = i + 1
                right = len(nums) - 1
            else:
                continue
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
                    right -= 1
                    while left < right and nums[right + 1] == nums[right]:
                        right -= 1
                else:
                    if nums[i] + nums[left] + nums[right] < 0:
                        left += 1
                    else:
                        right -= 1
        return result
```

itertools

```python

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        result = []
        import itertools
        for i in itertools.combinations(nums, 3):
            if sum(i) == 0:
                lst = sorted(list(i))
                if lst not in result:
                    result.append(lst)
        return result

```

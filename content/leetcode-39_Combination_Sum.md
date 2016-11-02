Title: 39. Combination Sum 
Date: 2016-09-29 23:58
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-39_Combination_Sum 
Authors: Weezer Su
Summary: Combination Sum
Boundry, eeewwww

```python
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.result = []
        for i in range(len(candidates)):
            self.recursivesum([candidates[i]], candidates[i:], target)

        return self.result

    def recursivesum(self, temp_list, comblist, target):
        if sum(temp_list) == target:
            self.result.append(temp_list)
            return
        for i in range(len(comblist)):
            if sum(temp_list) + comblist[i] == target:
                result_list = temp_list[:]
                result_list.append(comblist[i])
                self.result.append(result_list)
            if sum(temp_list) + comblist[i] < target:
                test_list = temp_list[:]
                test_list.append(comblist[i])
                self.recursivesum(test_list[:], comblist[i:], target)



```


Title:90. Subsets II
Date: 2017-03-04 16:27
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-90-Subsets-II 
Authors: Weezer Su
Summary:Subsets II 


```python
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        lst = [[]]
        nums.sort()
        for i in nums:
            len_lst = len(lst)
            for j in xrange(len_lst):
                element_copy = lst[j][:]
                element_copy.append(i)
                if element_copy not in lst:
                    lst.append(element_copy)
        return lst
```


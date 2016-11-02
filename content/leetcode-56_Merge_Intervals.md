Title: 56. Merge Intervals 
Date: 2016-11-01 00:17
Category: leetcode
Tags: code, python, leetcode
Slug:leetcode-56_Merge_Intervals 
Authors: Weezer Su
Summary: Merge Intervals

这题到底想干什么？
```python
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        return_lst = []
        for pos, val in enumerate(sorted(intervals, key=lambda Interval: Interval.start)):
            if len(return_lst) == 0:
                return_lst.append(val)
                continue
            if return_lst[-1].end >= val.start:
                return_lst[-1].end = max(val.end, return_lst[-1].end)
                continue
            return_lst.append(val)
        return return_lst
```


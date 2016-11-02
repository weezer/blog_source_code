Title: 57. Insert Interval
Date: 2016-11-01 00:19
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-57_Insert_Intervals 
Authors: Weezer Su
Summary:  Insert Interval

我感觉我做错了。
```python
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        # Definition for an interval.
        intervals.append(newInterval)
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


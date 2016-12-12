Title: 80. Remove Duplicates from Sorted Array II 
Date: 2016-12-01 00:07
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-80_Remove_Duplicates_from_Sorted_Array_II 
Authors: Weezer Su
Summary: Remove Duplicates from Sorted Array II


```python
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = {}
        for i in nums:
            if k.get(i) >= 2:
                continue
            elif k.get(i):
                k[i] += 1
            else:
                k[i] = 1
        print k
        k.keys().sort

        print int(''.join([(str(i) * k[i]) for i in k.keys()]))

```


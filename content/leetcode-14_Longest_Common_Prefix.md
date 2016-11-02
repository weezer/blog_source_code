Title: 14. Longest Common Prefix 
Date: 2016-09-18 23:00
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-14_Longest_Common_Prefix 
Authors: Weezer Su
Summary: Longest Common Prefix

pytho support Short-circuit evaluation, left to right, python is lazy and lazy is virtue.


```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0 or len(strs[0]) == 0:
            return ""
        prefix = ""
        count = 0
        flag = True
        while True:
            for i in strs:
                if count >= len(i):
                    return prefix
                compare_letter = strs[0][count]
                if compare_letter == i[count]:
                    continue
                else:
                    flag = False 
                    break
            count += 1
            if not flag:
                break
            prefix += compare_letter
        return prefix
            
```

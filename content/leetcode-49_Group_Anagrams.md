Title: 49. Group Anagrams 
Date: 2016-10-16 14:23
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-49_Group_Anagrams 
Authors: Weezer Su
Summary: Group Anagrams

Piece of cake

```python
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d= {}
        for i in strs:
            str_key = ''.join(sorted(list(i)))
            if d.has_key(str_key):
                d[str_key].append(i)
            else:
                d[str_key] = [i]
        return d.values()
```


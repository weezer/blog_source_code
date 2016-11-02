Title: 28. Implement strStr() 
Date: 2016-09-21 22:07
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-28_Implement_strStr 
Authors: Weezer Su
Summary: Implement strStr()

I dont know how to write [KMP](http://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html)
another good article about [KMP](http://blog.csdn.net/v_july_v/article/details/7041827)

```python
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        if len(haystack) == 0 or len(needle) == 0:
            return -1
        p_needle = 0
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
```


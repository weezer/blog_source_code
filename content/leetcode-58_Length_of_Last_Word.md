Title: 58. Length of Last Word
Date: 2016-11-01 00:27
Category: leetcode
Tags: code, python, leetcode
Slug:leetcode-58_Length_of_Last_Word 
Authors: Weezer Su
Summary: Length of Last Word

真好，全是这种题就好了。
```python
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s.replace(" ", "")) == 0:
            return 0
        return len(s.split()[-1])
```


Title:87. Scramble String 
Date: 2017-02-21 13:47
Category: leetcode
Tags: code, python, leetcode
Slug:leetcode-87-Scramble-String 
Authors: Weezer Su
Summary: 87. Scramble String
题目写的不好，前后转换也是可以的 great == reatg

```python
ass Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False
        if sorted(s1) != sorted(s2):
            return False

        for i in range(1, len(s1)):
            s11 = s1[:i]
            s12 = s1[i:]
            s21 = s2[:i]
            s22 = s2[i:]
            if self.isScramble(s11, s21) and self.isScramble(s12, s22):
                return True
            s21 = s2[-i:]
            s22 = s2[:-i]
            if self.isScramble(s11, s21) and self.isScramble(s12, s22):
                return True
        return False
```


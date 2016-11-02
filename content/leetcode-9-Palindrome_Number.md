Title: 09. Palindrome Number
Date: 2016-09-17 22:43
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-9-Palindrome_Number
Authors: Weezer Su
Summary:  Palindrome Number

noob question, and EXTRA SPACE means u can use variables but u cant use stack, list.

```python
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        maxInt = (1 << 31)
        if x >= maxInt - 1 or x < 0:
            return False
        if x == int(str(x)[::-1]):
            return True
        return False
        
```

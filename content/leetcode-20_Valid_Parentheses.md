Title: 20. Valid Parentheses 
Date: 2016-09-21 00:20
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-20_Valid_Parentheses 
Authors: Weezer Su
Summary: Valid Parentheses

Watch this
```python
a = []
not a == False
b = [1]
not b == True
```

tricky python, very tricky.

```python
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if i in ('([{'):
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if i == ')' and stack[-1] != '(' or i == ']' and stack[-1] != '[' or i == '}' and stack[-1] != '{':
                    return False
                stack.pop()
        return not stack
```


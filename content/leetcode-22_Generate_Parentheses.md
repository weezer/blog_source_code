Title: 22. Generate Parentheses 
Date: 2016-09-21 11:38
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-22_Generate_Parentheses 
Authors: Weezer Su
Summary: Generate Parentheses

Go over recursion.


```python
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.result = []
        if n == 0:
            return self.result
        self.rec(n, n, '')
        return self.result
        
    def rec(self, left, right, input):
        if left > right:
            return
        if left == 0 and right == 0:
            self.result.append(input)
        if left > 0:
            self.rec(left - 1, right, input + '(')
        if right > 0:
             self.rec(left, right - 1, input + ')')
            
        
       
```


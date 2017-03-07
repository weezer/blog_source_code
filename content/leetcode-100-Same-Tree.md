Title:100. Same Tree 
Date: 2017-03-05 20:57
Category: leetcode
Tags: code, python, leetcode
Slug:leetcode-100-Same-Tree 
Authors: Weezer Su
Summary: 100. Same Tree
``` a=None, b=None. a == b is True ```
只要没有出现false就是true
```python
class Solution(object):
    def isSameTree(self, p, q):
        if p == q:
            return True
        if p is None or q is None or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

